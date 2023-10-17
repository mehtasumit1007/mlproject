import sys
import logging

def error_message_details(error, error_details):
    exc_type, exc_value, exc_traceback = error_details
    file_name = exc_traceback.tb_frame.f_code.co_filename
    error_message = f"Error occurred in Python script name [{file_name}] line number [{exc_traceback.tb_lineno}] error message [{error}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, exception):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, sys.exc_info())
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message

# Example usage:
try:
    # Some code that might raise an exception
    x = 1 / 0
except Exception as e:
    custom_exception = CustomException("Division by zero", e)
    raise custom_exception  # Raise the custom exception
