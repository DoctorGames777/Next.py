from .Animal import Animal  # Import the Animal class from the same package


class Cat(Animal):
    """
    A class representing a cat in the zoo, inheriting from Animal.
    """
    def talk(self):
        """
        Make a sound characteristic of a cat.

        This method overrides the talk method in the Animal class.
        """
        print("meow")

    def chase_laser(self):
        """
        Perform a chasing action towards a laser pointer.
        """
        print("Meeeeow")
