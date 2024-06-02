import functools


def check_id_valid(id_number):
    """
    Check if an Israeli ID number is valid using the Luhn algorithm.

    :param id_number: The ID number to validate (int)
    :return: True if the ID number is valid, False otherwise (bool)
    """
    # Convert the ID number to a list of its digits
    list_of_digits = [int(digit) for digit in str(id_number)]

    # Double every second digit and sum the digits of the resulting numbers
    doubled_and_summed_digits = [
        num % 10 + num // 10  # Sum the digits of the number
        for i, num in enumerate(
            list_of_digits[i] * 1 if i % 2 == 0 else list_of_digits[i] * 2
            for i in range(len(list_of_digits))
        )
    ]

    # Calculate the total sum of the processed digits
    total_sum = functools.reduce(lambda a, b: a + b, doubled_and_summed_digits)

    # Check if the total sum modulo 10 is 0 (valid ID)
    return total_sum % 10 == 0
