import sys
from mlproject.logger import logging

def error_message_detail(error, error_message: str):
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script: [{0}] at line number: [{1}], error message: {error_message}"
    file_name,exc_tb.tb_lineno, str(error)
    return error_message






class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_details, error_message)

    def __str__(self):
        return self.error_message