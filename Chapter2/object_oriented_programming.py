from Chapter2.Zoo.Animal import Animal
from Chapter2.Zoo.Dog import Dog
from Chapter2.Zoo.Cat import Cat
from Chapter2.Zoo.Skunk import Skunk
from Chapter2.Zoo.Unicorn import Unicorn
from Chapter2.Zoo.Dragon import Dragon


def main():
    """
    Main function to simulate a zoo with different types of animals.

    The function creates instances of various animal classes, adds them to a zoo list,
    checks if each animal is hungry, feeds them until they are no longer hungry,
    makes them perform their specific actions, and finally prints the zoo name.

    :return: None
    """
    # Create instances of various animals
    animal1 = Dog("Brownie", 10)
    animal2 = Cat("Zelda", 3)
    animal3 = Skunk("Stinky")
    animal4 = Unicorn("Keith", 7)
    animal5 = Dragon("Lizzy", 1450)

    # Add animals to the zoo list
    zoo_lst = [animal1, animal2, animal3, animal4, animal5]

    # Add more animals to the zoo list
    zoo_lst.append(Dog("Doggo", 80))
    zoo_lst.append(Cat("Kitty", 80))
    zoo_lst.append(Skunk("Stinky Jr", 80))
    zoo_lst.append(Unicorn("Clair", 80))
    zoo_lst.append(Dragon("McFly", 80))

    # Iterate over each animal in the zoo list
    for animal in zoo_lst:
        # Check if the animal is hungry
        if animal.is_hungry():
            print("{} {}".format(type(animal).__name__, animal.get_name()))
            # Feed the animal until it is no longer hungry
            while animal.is_hungry():
                animal.feed()
        # Make the animal talk
        animal.talk()

        # Perform specific actions based on the type of animal
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    # Print the name of the zoo
    print(Animal.zoo_name)


if __name__ == "__main__":
    main()
