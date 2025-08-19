import sys

def error_message_detail(error, error_detail: sys):
    """
    This function takes an error and its details, and returns a formatted string
    containing the error message and the file name where the error occurred.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script: [{file_name}] line number: [{exc_tb.tb_lineno}] error message: [{str(error)}]"
    return error_message


class CustomException(Exception):
    """
    Custom exception class that inherits from the built-in Exception class.
    It is used to raise exceptions with a detailed error message.
    """
    def __init__(self, error_message ,error_detail: str):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)    

    def __str__(self):
        return self.error_message
    
