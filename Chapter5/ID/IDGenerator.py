from .IDValidator import check_id_valid


def id_generator(id_number):
    """
    Generate valid Israeli ID numbers starting from a given number.

    :param id_number: The starting number for generating IDs (int)
    :yield: Valid Israeli ID numbers (int)
    """
    for id_number in range(id_number, 1000000000):
        if check_id_valid(id_number):
            yield id_number
