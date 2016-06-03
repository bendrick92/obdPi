#!/usr/bin/python
#
# HD44780 LCD/OLED Test Script for
# Raspberry Pi
#
# Author : Robert Coward/Paul Carpenter (based on driver by Matt Hawkins/)
# Site   : http://www.raspberrypi-spy.co.uk
#          http://www.pcserviceslectronics.co.uk
#
# Date   : 02/03/2014
#

# The wiring for the LCD is as follows:
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)       - GROUND THIS PIN
# 6 : Enable or Strobe
# 7 : Data Bit 0             - NOT USED
# 8 : Data Bit 1             - NOT USED
# 9 : Data Bit 2             - NOT USED
# 10: Data Bit 3             - NOT USED
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND

#import
import RPi.GPIO as GPIO
import time
import subprocess
import os
import math
import datetime

class OledManager():
  # ASCII character defintion
  char_block = chr(219)

  # Define GPIO to LCD mapping (USES BCM MODE NUMBERING scheme)
  #LCD_RS = 22
  LCD_RS = 26
  LCD_E  = 17
  LCD_D4 = 25
  LCD_D5 = 18
  LCD_D6 = 24
  LCD_D7 = 23

  # Generate an array of pin numbers to write out for the data lines
  lcdPins = [LCD_D7, LCD_D6, LCD_D5, LCD_D4]

  # Define some device constants
  LCD_WIDTH = 16    # Maximum characters per line
  LCD_CHR = True
  LCD_CMD = False

  LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
  LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

  # Timing constants for low level write operations
  # NOTE: Enable cycle time must be at least 1 microsecond
  # NOTE2: Actually, these can be zero and the LCD will typically still work OK
  EDEL_TAS =  0.00001      # Address setup time (TAS)
  EDEL_PWEH = 0.00001      # Pulse width of enable (PWEH)
  EDEL_TAH =  0.00001      # Address hold time (TAH)

  # Timing constraints for initialisation steps - IMPORTANT!
  # Note that post clear display must be at least 6.2ms for OLEDs, as opposed
  # to only 1.4ms for HD44780 LCDs. This has caused confusion in the past.
  DEL_INITMID = 0.01       # middle of initial write (min 4.1ms)
  DEL_INITNEXT = 0.0002    # post second initial write (min 100ns)
  DEL_POSTCLEAR = 0.01     # post clear display step (busy, min 6.2ms)

  def __init__(self):
    self.lcd_init()

  # ==============================================================================
  # LCD Initialisation to setup the two line display using the 4 bit interface

  def lcd_init(self):
    # Configure the GPIO to drive the LCD display correctly
    GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers

    # setup all output pins for driving LCD display
    GPIO.setup(self.LCD_E, GPIO.OUT)  # E
    # PC - better safe starting state
    GPIO.output(self.LCD_E, 0)        # set low as idle state
    GPIO.setup(self.LCD_RS, GPIO.OUT) # RS
    # PC - more maintainable initialisation
    for val in self.lcdPins:          # enable DB7 to DB4
      GPIO.setup(val, GPIO.OUT)
      GPIO.output(val, 0)        # set low

    # Initialise display into 4 bit mode, using recommended delays
    self.lcd_byte(0x33, self.LCD_CMD, self.DEL_INITNEXT, self.DEL_INITMID)
    self.lcd_byte(0x32, self.LCD_CMD, self.DEL_INITNEXT)

    # Now perform remainder of display init in 4 bit mode - IMPORTANT!
    # These steps MUST be exactly as follows, as OLEDs in particular are rather fussy
    self.lcd_byte(0x28, self.LCD_CMD, self.DEL_INITNEXT)    # two lines and correct font
    self.lcd_byte(0x08, self.LCD_CMD, self.DEL_INITNEXT)    # display OFF, cursor/blink off
    self.lcd_byte(0x01, self.LCD_CMD, self.DEL_POSTCLEAR)   # clear display, waiting for longer delay
    self.lcd_byte(0x06, self.LCD_CMD, self.DEL_INITNEXT)    # entry mode set

    # extra steps required for OLED initialisation (no effect on LCD)
    self.lcd_byte(0x17, self.LCD_CMD, self.DEL_INITNEXT)    # character mode, power on

    # now turn on the display, ready for use - IMPORTANT!
    self.lcd_byte(0x0C, self.LCD_CMD, self.DEL_INITNEXT)    # display on, cursor/blink off

  # ==============================================================================
  # Outputs string of characters to the LCD display line, padding as required
  # NOTE: Incoming string MUST be a string of simple characters with no complex
  # unicode types present, as otherwise incorrect encoding will occur.

  def lcd_string(self, message):
    # Send string to display, padding with spaces if required
    message = message.ljust(self.LCD_WIDTH," ")

    for i in range(self.LCD_WIDTH):
      # output a single byte value for the incoming character
      self.lcd_byte(ord(message[i]), self.LCD_CHR)

  # ==============================================================================
  # Low level routine to output a byte of data to the LCD display
  # over the 4 bit interface. Two nybbles are sent, one after the other.
  # The post_delay specifies optional delay to cover busy periods
  # The mid_delay specifies optional delay between the 4 bit nibbles (special case)

  def lcd_byte(self, byteVal, mode, post_delay = 0, mid_delay = 0):

    # convert incoming value into 8 bit array, padding as required
    bits = bin(byteVal)[2:].zfill(8)

    # set mode = True  for character, False for command
    GPIO.output(self.LCD_RS, mode) # RS

    # Output the four High bits
    for i in range(4):
      GPIO.output(self.lcdPins[i], int(bits[i]))

    # Toggle 'Enable' pin, wrapping with minimum delays
    time.sleep(self.EDEL_TAS)
    GPIO.output(self.LCD_E, True)
    time.sleep(self.EDEL_PWEH)
    GPIO.output(self.LCD_E, False)
    time.sleep(self.EDEL_TAH)

    # Wait for extra mid delay if specified (special case)
    if mid_delay > 0:
      time.sleep(mid_delay)

    # Output the four Low bits
    for i in range(4,8):
      GPIO.output(self.lcdPins[i-4], int(bits[i]))

    # Toggle 'Enable' pin, wrapping with minimum delays
    time.sleep(self.EDEL_TAS)
    GPIO.output(self.LCD_E, True)
    time.sleep(self.EDEL_PWEH)
    GPIO.output(self.LCD_E, False)
    time.sleep(self.EDEL_TAH)

    # Wait for extra post delay if specified (covers busy period)
    if post_delay > 0:
      time.sleep(post_delay)

  def clear_screen(self):
    self.output_message("", "")

  def output_message_line_1(self, message):
    self.lcd_byte(self.LCD_LINE_1, self.LCD_CMD)
    self.lcd_string(message)

  def output_message_line_2(self, message):
    self.lcd_byte(self.LCD_LINE_2, self.LCD_CMD)
    self.lcd_string(message)

  def output_message(self, *args):
    line_1 = ""
    line_2 = ""

    if len(args) == 1:
      if len(args[0]) < 16:
        line_1 = args[0]
      else:
        line_1 = args[0][:16]
        line_2 = args[0][16:]
    elif len(args) == 2:
      line_1 = args[0]
      line_2 = args[1]

    self.output_message_line_1(line_1)
    self.output_message_line_2(line_2)

  def clean_gpio(self):
    GPIO.cleanup()

  def clean_and_clear(self):
    self.clear_screen()
    self.clean_gpio()

  def oled_event_decorator(self, event_name):
    def decorator(func):
      def func_wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        output = event_name
        if not event_name == "":
          output += ": "
        self.output_message(output + str(result))
        return result
      return func_wrapper
    return decorator