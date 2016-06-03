import logging
import os
from datetime import datetime


class LogManager:

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    LOGS_DIR = os.path.join(BASE_DIR, 'logs/')

    def __init__(self, log_file_path_sub=''):
        self.full_log_file_path = os.path.join(self.LOGS_DIR, log_file_path_sub)
        if not os.path.exists(self.full_log_file_path):
            os.makedirs(self.full_log_file_path)
        self.log_file_name = self.full_log_file_path + self.get_timestamp_string() + '.log'
        logging.basicConfig(filename=self.log_file_name, level=logging.DEBUG, format='%(asctime)s: %(message)s')

    def add_info_entry_to_log(self, info_text):
        logging.info(str(info_text))

    def add_debug_entry_to_log(self, debug_text):
        logging.debug(str(debug_text))

    def add_warning_entry_to_log(self, warning_text):
        logging.warning(str(warning_text))

    def get_timestamp_string(self):
        return str(datetime.now().strftime('%Y%m%d_%H%M%S'))

    def log_event_decorator(self, event_name, event_type):
        def decorator(func):
            def func_wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                output = str(event_name) + ": " + str(result)
                if str(event_type) == "INFO":
                    self.add_info_entry_to_log(output)
                elif str(event_type) == "DEBUG":
                    self.add_debug_entry_to_log(output)
                elif str(event_type) == "WARNING":
                    self.add_warning_entry_to_log(output)
                else:
                    self.add_info_entry_to_log(output)
                return result

            return func_wrapper

        return decorator
