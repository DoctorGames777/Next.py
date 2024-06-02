class Animal:
    """
    A class representing an animal in the zoo.
    """
    zoo_name = "Hayaton"  # Shared attribute for all animals in the zoo

    def __init__(self, name, hunger=0):
        """
        Initialize an Animal object with a name and hunger level.

        :param name: The name of the animal (str)
        :param hunger: The hunger level of the animal (int, default 0)
        """
        self._name = name  # Name of the animal
        self._hunger = hunger  # Hunger level of the animal

    def get_name(self):
        """
        Get the name of the animal.

        :return: The name of the animal (str)
        """
        return self._name

    def is_hungry(self):
        """
        Check if the animal is hungry.

        :return: True if the animal is hungry, False otherwise (bool)
        """
        return self._hunger > 0

    def feed(self):
        """
        Feed the animal by reducing its hunger level by 1.
        """
        self._hunger -= 1

    def talk(self):
        """
        A placeholder method for the animal to make a sound.
        This method should be overridden in subclasses.
        """
        pass
