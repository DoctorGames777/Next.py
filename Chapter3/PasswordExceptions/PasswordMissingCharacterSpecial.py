from .PasswordMissingCharacter import PasswordMissingCharacter


class PasswordMissingCharacterSpecial(PasswordMissingCharacter):
    """
    Exception raised when a password is missing a special character.
    """

    def __str__(self, problem):
        """
        Return a string representation of the exception.

        Appends specific information about the missing character type to the generic error message.

        :param problem: The parent exception instance
        :return: Error message as a string
        """
        return PasswordMissingCharacter.__str__(problem) + " (Special)"
