import os
import sys


class DefaultException(Exception):
    """This class raise an exception on error and giver file name and line number where error occured.

    Args:
        Exception (_type_): object of exception
    """

    def __init__(self, error_message: Exception, error_detail: sys) -> None:
        super().__init__(error_message)
        self.error_message = DefaultException.get_detailed_error_message(error_message=error_message,
                                                                         error_detail=error_detail
                                                                         )

    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_detail: sys) -> str:
        """This function create a error message in given format

        Args:
            error_message (Exception): Exception object
            error_detail (sys): object of sys module

        Returns:
            str: error_message
        """
        _, _, exec_tb = error_detail.exc_info()
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"Error occured in script: [{file_name}] at line number: [{line_number}]. Error message is: [{error_message}]"
        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self) -> str:
        return DefaultException.__name__.str()
