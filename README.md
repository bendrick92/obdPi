## Summary
A python project to pull vehicle information from a bluetooth OBD-II adapter and output to a 16x2 OLED display.

## Hardware
The following hardware is required for functionality of the OLED scripts:

* 16x2 character OLED from Adafruit ([link](https://www.adafruit.com/products/823))
* OBD-II Bluetooth adapter ([link](http://www.amazon.com/Veepeak-Bluetooth-Scanner-Automotive-Diagnostic/dp/B011NSX27A))
* USB Bluetooth adapter ([link](http://www.amazon.com/Kinivo-BTD-300-Bluetooth-Energy-adapter/dp/B005Z5HT2M))
* Wiring option A
    * 22 AWG stranded hook-up wire ([link](https://www.sparkfun.com/products/11375))
    * 56 count 0.1" female crimp pins ([link](https://www.pololu.com/product/1930))
* Wiring option B
   * Pre-crimped hook-up wire ([link](https://www.pololu.com/category/71/wires-with-pre-crimped-terminals))
* 1 count 1x16 pin crimp connector housing ([link](https://www.pololu.com/product/1920))
* 1 count 2x20 pin crimp connector housing ([link](https://www.pololu.com/product/1992))
* 56 (1x16, 2x20) pin count 0.1" break-away male header ([link](https://www.pololu.com/product/965))

## OLED Wiring

Reference pinout images:

* [OLED](http://i.imgur.com/RcIjjdA.jpg) 
* [Raspberry Pi 2](http://i.imgur.com/FCB5swt.png)

Pinout map:

| GPIO pin | OLED pin |
| --- | ---|
| 2 | 2 |
| 6 | 1 |
| 11 | 6 |
| 12 | 12 |
| 16 | 14 |
| 18 | 13 |
| 20 | 5 |
| 22 | 11 |
| 37 | 4 |

## Code

* /obdpi - Contains the modules for the project as '*_manager.py' files
* /tests - Contains unit tests for several of the modules
* main_oled.py - Main script to run for output to the OLED
* main_print.py - Secondary script to run for output to console (no OLED necessary)

## Dependencies

* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [python-OBD](https://github.com/brendan-w/python-OBD)
* RPi.GPIO
