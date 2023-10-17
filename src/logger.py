import sys
import logging

# Initialize the logger
logger = logging.getLogger(__name)

def error_message_details(error, error_details):
    _, _, exc_tb = error_details
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details=error_details)
        logger.error(self.error_message)  # Log the error message

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        # Some code that might raise an exception
        x = 1 / 0
    except Exception as e:
        custom_exception = CustomException("Division by zero", sys.exc_info())
