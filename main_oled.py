import atexit
import sys
from time import sleep

import obdpi.shared_settings
from obdpi.log_manager import LogManager
from obdpi.obd_manager import ObdManager
from obdpi.oled_manager import OledManager
from obdpi.serial_manager import SerialManager

log_man = LogManager()
oled_man = OledManager()
ser_man = SerialManager()
obd_man = ObdManager()


@oled_man.oled_event_decorator("Ser Conn")
@log_man.log_event_decorator("Initialize Serial Connection", "INFO")
def init_serial(is_testing, environment):
    try:
        ser_man.init_serial_connection(is_testing, environment)
        if ser_man.has_serial_connection():
            return "SUCCESS"
        else:
            return "FAIL"
    except Exception, e:
        return "[EXCEPTION] " + str(e)


@oled_man.oled_event_decorator("OBD Conn")
@log_man.log_event_decorator("Initialize OBD Connection", "INFO")
def init_obd(connection_id):
    try:
        obd_man.init_obd_connection(connection_id)
        if obd_man.has_obd_connection():
            return "SUCCESS"
        else:
            return "FAIL"
    except Exception, e:
        return "[EXCEPTION] " + str(e)


@oled_man.oled_event_decorator("")
@log_man.log_event_decorator("OBD Response", "INFO")
def get_obd_response(obd_command):
    try:
        obd_response = str(obd_man.generate_obd_response(obd_command))
        return obd_response
    except Exception, e:
        return "[EXCEPTION] " + str(e)


def start(cmd):
    while True:
        if init_serial(obdpi.shared_settings.is_testing, obdpi.shared_settings.environment):
            if init_obd(ser_man.connection_id):
                break
        sleep(1.0)
    while True:
        obd_response = str(get_obd_response(cmd))
        sleep(0.15)     # May need to adjust for clean interruption upon shutdown


@oled_man.oled_event_decorator("Ending Script")
@log_man.log_event_decorator("Ending Script", "INFO")
def end():
    oled_man.clean_and_clear()
    sys.exit()


if __name__ == "__main__":
    if len(sys.argv) > 1: 
        obd_command = str(sys.argv[1])
    elif obdpi.shared_settings.obd_command is not None:
        obd_command = str(obdpi.shared_settings.obd_command)
    else:
        obd_command = "RPM"

    atexit.register(end)
    start(obd_command)
