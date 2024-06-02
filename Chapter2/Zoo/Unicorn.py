from .Animal import Animal  # Import the Animal class from the same package


class Unicorn(Animal):
    """
    A class representing a unicorn in the zoo, inheriting from Animal.
    """
    def talk(self):
        """
        Make a sound characteristic of a unicorn.

        This method overrides the talk method in the Animal class.
        """
        print("Good day, darling")

    def sing(self):
        """
        Perform a singing action characteristic of a unicorn.
        """
        print("I’m not your toy...")
