class PasswordMissingCharacter(Exception):
    """
    Exception raised when a password is missing a required character type.
    """

    def __init__(self, password):
        """
        Initialize the exception with the password causing the issue.

        :param password: The password that is missing a character (str)
        """
        self._password = password

    def __str__(self):
        """
        Return a string representation of the exception.

        This method provides a generic error message indicating that the password is missing a character.

        :return: Error message as a string
        """
        return "The password is missing a character"
