from .Animal import Animal  # Import the Animal class from the same package


class Dog(Animal):
    """
    A class representing a dog in the zoo, inheriting from Animal.
    """
    def talk(self):
        """
        Make a sound characteristic of a dog.

        This method overrides the talk method in the Animal class.
        """
        print("woof woof")

    def fetch_stick(self):
        """
        Perform a fetching action with a stick.
        """
        print("There you go, sir!")
