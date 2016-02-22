# obdPi
A Python-based project to pull vehicle information from a bluetooth OBD-II adapter and output to a 16x2 OLED display.

# Files
test.py: A test script to output OBD-II data to the console. 
test_oled.py: A test script to output OBD-II data to an attached OLED display.  Utilizes oled_manager.py.
oled_manager.py: A script to manage connections and data transfer to/from an attached OLED display.  Requires a correctly wired OLED display.  See https://goo.gl/photos/HpfFGQXt2RRXrZhK8 for example.
