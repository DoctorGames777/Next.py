from .Animal import Animal  # Import the Animal class from the same package


class Dragon(Animal):
    """
    A class representing a dragon in the zoo, inheriting from Animal.
    """
    def __init__(self, name, hunger=0, color="Green"):
        """
        Initialize a Dragon object with a name, hunger level, and color.

        :param name: The name of the dragon (str)
        :param hunger: The hunger level of the dragon (int, default 0)
        :param color: The color of the dragon (str, default "Green")
        """
        super().__init__(name, hunger)
        self._color = color  # Color of the dragon

    def talk(self):
        """
        Make a sound characteristic of a dragon.

        This method overrides the talk method in the Animal class.
        """
        print("Raaaawr")

    def breath_fire(self):
        """
        Emit a characteristic fire breath associated with dragons.
        """
        print("$@#$#@$")
