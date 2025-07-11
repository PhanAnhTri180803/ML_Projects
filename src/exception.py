#import package
import sys

def error_message_detail(errors,error_detail:sys):
    """
    This function will return the error message
    """
    
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"""
    Error occurred in script: [{file_name}] 
    line number: [{exc_tb.tb_lineno}] 
    error message: [{str(errors)}]
    """
    return error_message

# Custom Exception Class
class CustomException(Exception):
    def __init__(self, errors, error_detail:sys):
        super().__init__(error_message_detail(errors, error_detail))
        self.errors = errors
        self.error_detail = error_detail

    def __str__(self):
        return self.error_message_detail(self.errors, self.error_detail)
