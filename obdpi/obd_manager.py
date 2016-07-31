import obd


class ObdManager:

    def __init__(self):
        self.obd_connection = ""

    def init_obd_connection(self, serial_connection_id):
        if obd.scan_serial():
            if serial_connection_id in obd.scan_serial():
                self.obd_connection = obd.OBD(serial_connection_id)

    def has_obd_connection(self):
        if self.obd_connection != "":
            if self.obd_connection.is_connected():
                return True
            else:
                return False
        else:
            return False

    def generate_obd_response(self, command):
        if self.has_obd_connection():
            if command == "RPM":
                obd_command = obd.commands.RPM
                obd_unit = "RPM"
            elif command == "BOOST":
                obd_command = obd.commands.INTAKE_PRESSURE
                obd_unit = "PSI"
            else:
                return "'" + command + "' is unrecognized OBD command"
                
            obd_response = self.obd_connection.query(obd_command)
            
            if not obd_response.is_null():
                converted_obd_response = round(obd_response.value.to("psi").magnitude, 3)
                return str(converted_obd_response) + " " + obd_unit
            else:
                return "No OBD response"
        else:
            return "No OBD connection"
