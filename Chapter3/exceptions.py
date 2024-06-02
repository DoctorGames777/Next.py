import string
from Chapter3.UsernameExceptions.UsernameTooShort import UsernameTooShort
from Chapter3.UsernameExceptions.UsernameTooLong import UsernameTooLong
from Chapter3.UsernameExceptions.UsernameContainsIllegalCharacter import UsernameContainsIllegalCharacter
from Chapter3.PasswordExceptions.PasswordTooShort import PasswordTooShort
from Chapter3.PasswordExceptions.PasswordTooLong import PasswordTooLong
from Chapter3.PasswordExceptions.PasswordMissingCharacter import PasswordMissingCharacter
from Chapter3.PasswordExceptions.PasswordMissingCharacterUppercase import PasswordMissingCharacterUppercase
from Chapter3.PasswordExceptions.PasswordMissingCharacterLowercase import PasswordMissingCharacterLowercase
from Chapter3.PasswordExceptions.PasswordMissingCharacterDigit import PasswordMissingCharacterDigit
from Chapter3.PasswordExceptions.PasswordMissingCharacterSpecial import PasswordMissingCharacterSpecial


def check_input(username, password):
    """
    Check the validity of a username and password based on specific criteria.

    :param username: str - The username to be validated
    :param password: str - The password to be validated
    :return: None
    :raises UsernameTooShort: If the username is shorter than 3 characters
    :raises UsernameTooLong: If the username is longer than 16 characters
    :raises UsernameContainsIllegalCharacter: If the username contains illegal characters
    :raises PasswordTooShort: If the password is shorter than 8 characters
    :raises PasswordTooLong: If the password is longer than 40 characters
    :raises PasswordMissingCharacter: If the password is missing a required character
    """
    try:
        # Check if the username is too short
        if len(username) < 3:
            raise UsernameTooShort(username)
        # Check if the username is too long
        elif len(username) > 16:
            raise UsernameTooLong(username)
        # Check if the username contains illegal characters
        elif not username.replace('_', '').isalnum():
            raise UsernameContainsIllegalCharacter(username)
        # Check if the password is too short
        elif len(password) < 8:
            raise PasswordTooShort(password)
        # Check if the password is too long
        elif len(password) > 40:
            raise PasswordTooLong(password)
        # Check if the password is missing required characters
        elif (list(filter(lambda char: char in string.punctuation, password)) == [] or
              list(filter(lambda char: char.islower(), password)) == [] or
              list(filter(lambda char: char.isupper(), password)) == [] or
              list(filter(lambda char: char.isdigit(), password)) == []):
            raise PasswordMissingCharacter(password)
    except UsernameTooShort as problem:
        print(problem.__str__())
    except UsernameTooLong as problem:
        print(problem.__str__())
    except UsernameContainsIllegalCharacter as problem:
        print(problem.__str__())
    except PasswordTooShort as problem:
        print(problem.__str__())
    except PasswordTooLong as problem:
        print(problem.__str__())
    except PasswordMissingCharacter as problem:
        if list(filter(lambda char: char.isupper(), password)) == []:
            prob = PasswordMissingCharacterUppercase(password)
            print(PasswordMissingCharacterUppercase.__str__(prob, problem))
        elif list(filter(lambda char: char.islower(), password)) == []:
            prob = PasswordMissingCharacterLowercase(password)
            print(PasswordMissingCharacterLowercase.__str__(prob, problem))
        elif list(filter(lambda char: char.isdigit(), password)) == []:
            prob = PasswordMissingCharacterDigit(password)
            print(PasswordMissingCharacterDigit.__str__(prob, problem))
        elif list(filter(lambda char: char in string.punctuation, password)) == []:
            prob = PasswordMissingCharacterSpecial(password)
            print(PasswordMissingCharacterSpecial.__str__(prob, problem))
    else:
        print("OK")


def main():
    """
    Main function to test the check_input function with various usernames and passwords.

    :return: None
    """
    check_input("1", "2")  # The username is too short
    check_input("0123456789ABCDEFG", "2")  # The username is too long
    check_input("A_a1.", "12345678")  # The username contains an illegal character
    check_input("A_1", "2")  # The password is too short
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")  # The password is too long
    check_input("A_1", "abcdefghijklmnop")  # The password is missing a character (Uppercase)
    check_input("A_1", "ABCDEFGHIJLKMNOP")  # The password is missing a character (Lowercase)
    check_input("A_1", "ABCDEFGhijklmnop")  # The password is missing a character (Digit)
    check_input("A_1", "4BCD3F6h1jk1mn0p")  # The password is missing a character (Special)
    check_input("A_1", "4BCD3F6.1jk1mn0p")  # OK


if __name__ == "__main__":
    main()
