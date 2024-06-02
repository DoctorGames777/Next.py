class PasswordTooShort(Exception):
    """
    Exception raised when a password is too short.
    """

    def __init__(self, password):
        """
        Initialize the exception with the password causing the issue.

        :param password: The password that is too short (str)
        """
        self._password = password

    def __str__(self):
        """
        Return a string representation of the exception.

        This method provides a generic error message indicating that the password is too short.

        :return: Error message as a string
        """
        return "The password is too short"
