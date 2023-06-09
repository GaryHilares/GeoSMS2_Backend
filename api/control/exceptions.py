"""
NAME
    Exceptions - This file includes the exceptions used by GeoSMS.

FILE
    exceptions.py

CLASSES
    UnknownCommandException: Exception raised when a command is not known.
    WrongArguments: Exception raised when a command is called with incorrect arguments.

"""


class UnknownCommandException(Exception):
    """
    Exception raised when a command is not known.
    """

    def __init__(self, unknown_command=""):
        super().__init__(
            f"Command {unknown_command} is unknown."
            if unknown_command
            else "Unknown command."
        )


class WrongArgumentsException(Exception):
    """
    Exception raised when a command is called with incorrect arguments.
    """

    def __init__(self, command, wrong_arguments):
        super().__init__(f"{wrong_arguments} are not valid arguments for {command}.")
