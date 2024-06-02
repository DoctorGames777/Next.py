class UsernameContainsIllegalCharacter(Exception):
    """
    Exception raised when a username contains an illegal character.
    """

    def __init__(self, username):
        """
        Initialize the exception with the username causing the issue.

        :param username: The username containing the illegal character (str)
        """
        self._username = username

    def __str__(self):
        """
        Return a string representation of the exception.

        This method provides a descriptive error message indicating the illegal character and its index.

        :return: Error message as a string
        """
        # Find the first illegal character in the username
        illegal_char = next((char for char in self._username if not char.isalnum() and char != '_'), None)
        if illegal_char:
            index = self._username.find(illegal_char)
            return f"The username contains an illegal character, '{illegal_char}', at index {index}"
        else:
            return "The username contains an unknown illegal character"
