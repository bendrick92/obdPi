import obd
import sys
import time

if len(sys.argv) > 1:
    requestedCmd = str(sys.argv[1])
else:
    requestedCmd = ""

connection = obd.Async()
isConnected = connection.is_connected()

if isConnected:
    if requestedCmd == "RPM":
        cmd = obd.commands.RPM              #return engine RPM
    elif requestedCmd == "BOOST":
        cmd = obd.commands.INTAKE_PRESSURE  #return boost pressure
    else:
        cmd = obd.commands.RPM              #default return RPM

    def new_rpm(r):
        print "\r", str(r.value) + " " + str(r.unit), "Cmd: " + str(requestedCmd),
        time.sleep(0.1)

    connection.watch(cmd, callback=new_rpm)
    connection.start()

    time.sleep(60)
    connection.stop()
else:
    print "Not connected to any OBDII device"

connection.close()