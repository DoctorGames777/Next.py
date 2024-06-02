from .IDValidator import check_id_valid


class IDIterator:
    def __init__(self, id_number):
        """
        Initialize the IDIterator object with a starting ID number.

        :param id_number: The starting ID number for iteration (int)
        """
        self._id = id_number  # 100000000-999999999 => 9 digits number
        self.id_index = -1  # Initialize the index to -1, as the first ID will be at index 0

    def __iter__(self):
        """
        Make the IDIterator object an iterable.

        :return: The IDIterator object itself
        """
        return self

    def __next__(self):
        """
        Get the next valid Israeli ID number.

        :return: The next valid Israeli ID number (int)
        :raises StopIteration: When there are no more valid IDs to generate
        """
        while True:
            if self._id + self.id_index >= 1000000000:
                # If the current ID number exceeds the maximum limit, raise StopIteration
                raise StopIteration()
            self.id_index += 1  # Increment the index
            if check_id_valid(self._id + self.id_index):
                # If the current ID is valid, return it
                return self._id + self.id_index
