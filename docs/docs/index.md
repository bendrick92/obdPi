## Introduction

ObdPi is a Python 2.7 project designed for the Raspberry Pi to output a vehicle's OBD-II data to a 16x2 character OLED display.

## Installation

To get the latest project files for obdPi:

```
git clone https://github.com/bendrick92/obdPi.git
```

Or download the latest .zip [here](https://github.com/bendrick92/obdPi/archive/master.zip).

The latest release notes are always available [here](https://github.com/bendrick92/obdPi/releases/latest).

## Dependencies

* Python 2.7
* [PIP](https://pypi.python.org/pypi/pip) - Management of Python packages
* [python-OBD](https://github.com/brendan-w/python-OBD) - OBD-II serial module for reading engine data
* [RPi-GPIO](https://pypi.python.org/pypi/RPi.GPIO) - Control Raspberry Pi GPIO channels
* [pyserial](https://github.com/pyserial/pyserial) - Python serial port access library


## Setup

Use of the obdPi scripts requires a number of configuration steps, detailed instructions for each of which can be found [here](/setup).

## Usage

If you follow the aforementioned [Setup](/setup) steps, the obdPi script(s) should be set to execute upon startup of your Raspberry Pi.

These same scripts can also be manually executed.  If you have followed the steps to configure your external display, you can execute the `main_oled.py` via:

```
python main_oled.py
```

If not, you can still use `main_print.py` to output to the terminal via:

```
python main_print.py
```