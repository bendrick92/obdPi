import obd
import time
import sys
from oled_manager import OledManager

if len(sys.argv) > 1:
    requestedCmd = str(sys.argv[1])
else:
    requestedCmd = ""

is_testing = False
om = OledManager()

try:
    connection = obd.Async()
    isConnected = connection.is_connected()

    if isConnected:
        if requestedCmd == "RPM":
            cmd = obd.commands.RPM              #return engine RPM
        elif requestedCmd == "BOOST":
            cmd = obd.commands.INTAKE_PRESSURE  #return boost pressure
        else:
            cmd = obd.commands.RPM              #default return RPM

        def output(r):
            if is_testing:
                print "\r", str(r.value) + " " + str(r.unit)
            else:
                om.output_message(str(r.value), str(r.unit))

        connection.watch(cmd, callback=output)
        connection.start()

    else:
        if is_testing:
            print "\r" + "No connection"
        else:
            om.output_message('No connection', '                ')

    time.sleep(10)

    if isConnected:
        connection.stop()

    if not is_testing:
        om.clear_screen()
        om.clean()

    connection.close()

except (KeyboardInterrupt, SystemExit):
    if isConnected:
        connection.stop()

    if not is_testing:
        om.clear_screen()
        om.clean()

    connection.close()