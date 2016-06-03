class SerialManager:

    def __init__(self):
        self.connection_id = ""

    def init_serial_connection(self, is_testing, environment):
        if is_testing:
            if environment == "Windows":
                self.connection_id = "COM8080"
            elif environment == "Linux":
                self.connection_id = "/dev/pts/4"
        else:
            self.connection_id = "/dev/rfcomm0"

    def has_serial_connection(self):
        if self.connection_id != "":
            return True
        else:
            return False
