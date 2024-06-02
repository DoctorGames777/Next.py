class UsernameTooShort(Exception):
    """
    Exception raised when a username is too short.
    """

    def __init__(self, username):
        """
        Initialize the exception with the username causing the issue.

        :param username: The username that is too short (str)
        """
        self._username = username

    def __str__(self):
        """
        Return a string representation of the exception.

        This method provides a generic error message indicating that the username is too short.

        :return: Error message as a string
        """
        return "The username is too short"
