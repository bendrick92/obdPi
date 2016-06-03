class PrintManager:

    def print_message(self, message):
        print message

    def print_event_decorator(self, event_name):
        def decorator(func):
            def func_wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                output = str(event_name) + ": " + str(result)
                self.print_message(output)
                return result
            return func_wrapper
        return decorator
