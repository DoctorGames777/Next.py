class UsernameTooLong(Exception):
    """
    Exception raised when a username exceeds the allowed length.
    """

    def __init__(self, username):
        """
        Initialize the exception with the username causing the issue.

        :param username: The username that is too long (str)
        """
        self._username = username

    def __str__(self):
        """
        Return a string representation of the exception.

        This method provides a generic error message indicating that the username is too long.

        :return: Error message as a string
        """
        return "The username is too long"
