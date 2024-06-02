from .Animal import Animal  # Import the Animal class from the same package


class Skunk(Animal):
    """
    A class representing a skunk in the zoo, inheriting from Animal.
    """
    def __init__(self, name, hunger=0, stink_count=6):
        """
        Initialize a Skunk object with a name, hunger level, and stink count.

        :param name: The name of the skunk (str)
        :param hunger: The hunger level of the skunk (int, default 0)
        :param stink_count: The initial stink count of the skunk (int, default 6)
        """
        super().__init__(name, hunger)
        self._stink_count = stink_count  # Stink count of the skunk

    def talk(self):
        """
        Make a sound characteristic of a skunk.

        This method overrides the talk method in the Animal class.
        """
        print("tsssss")

    def stink(self):
        """
        Emit a characteristic odor associated with skunks.
        """
        print("Dear lord!")
