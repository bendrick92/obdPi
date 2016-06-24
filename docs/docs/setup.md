## Raspbian Setup

First, make sure your package lists are up-to-date:

```
sudo apt-get update
```

Confirm that Python is installed (should be included by default in your Raspbian installation):

```
python --version
```

Install Python setuptools to get PIP (the Python package manager):

```
sudo apt-get -y install python-pip
```

Install the python-OBD library via PIP:

```
sudo pip install obd
```

Install the RPi-GPIO library via PIP:

```
sudo pip install RPi.GPIO
```

Install the pyserial library:

```
sudo apt-get install python-serial
```

Next, enable auto-login to the 'pi' user (or whichever user you choose to run the scripts under):

```
sudo nano /etc/systemd/system/getty.target.wants/getty@tty1.service
```

Change the `ExecStart` line to:

```
ExecStart=-/sbin/agetty -a pi %I $TERM
```

---

## Daemon Setup

NOTE: This tutorial assumes you are using the latest release of Raspbian Jessie.  Information on daemon configuration in Jessie can be found [here](http://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/).

To have the obdPi scripts start on boot, you'll need to setup a daemon to execute the Python script for you.

First, create a new service script for the daemon:

```
sudo nano /lib/systemd/system/obdpi.service
```

For OLED applications, enter the following content in your new script:

```
[Unit]
Description=obdPi Service (OLED)
After=multi-user.target
[Service]
Type=idle
ExecStart=/usr/bin/python /path/to/scripts/main_oled.py
[Install]
WantedBy=multi-user.target
```

Or for non-OLED applications:

```
[Unit]
Description=obdPi Service (Print)
After=multi-user.target
[Service]
Type=idle
ExecStart=/usr/bin/python /path/to/scripts/main_print.py
[Install]
WantedBy=multi-user.target
```

Enable the daemon script:

```
sudo chmod 644 /lib/systemd/system/obdpi.service
sudo systemctl daemon-reload
sudo systemctl enable obdpi.service
```

Then reboot:

```
sudo reboot
```

After rebooting, confirm that the service is running:

```
sudo systemctl status obdpi.service
```

To stop the service:

```
sudo systemctl stop obdpi.service
```

And to disable the service (prevent it from starting at boot):

```
sudo systemctl disable obdpi.service
```

---

## Bluetooth Setup

To setup the Bluetooth connection between your Raspberry Pi and the OBD-II interface, first ensure the Bluetooth USB adapter is plugged into your Pi and the Bluetooth OBD-II adapter is installed in the vehicle's OBD-II port (and that both are within range of each other).

Next, install the basic Bluetooth utilities for Raspbian:

```
sudo apt-get install --no-install-recommends bluetooth
```

When the install is complete, make sure the Bluetooth service is running:

```
sudo service bluetooth status
```

Next, to configure the Bluetooth connection:

```
sudo bluetoothctl
agent on
default-agent
pairable on
scan on
```

The identifier for your Bluetooth OBD-II adapter should appear - be sure to take note of it. (AA:BB:CC:11:22:33 will be used as an example below).

```
scan off
pair AA:BB:CC:11:22:33
```

At this point, you may be prompted to enter an authentication pin.  Most adapters use, 0000, 1234 or require no pin (just press 'Enter').  Other adapters may require a specific pin, which would have been included on a slip with the adapter.

```
connect AA:BB:CC:11:22;33
quit
```

The Bluetooth connection should now be ready for use!

---

## Serial Connection

Once the Bluetooth connection has been configured, you'll need to bind it to a serial port.  Doing so allows you to communicate with the Bluetooth OBD-II adapter in Python.

One time configuration of the serial connection can be done with the following:

```
sudo rfcomm release all
sudo rfcomm bind 0 AA:BB:CC:11:22:33
```

To configure the serial connection at each boot (recommeded), simply add the aforementioned code before the end of the `/etc/rc.local`:

```
sudo nano /etc/rc.local
```

---

## Display Wiring

Utilization of the `main_oled.py` script requires a 16x2 character OLED display, as well as the assembly of a custom 40-pin to 16-pin cable.  A step-by-step guide for creating this cable can be found [here](/wiring).
