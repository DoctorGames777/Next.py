from Chapter5.ID.IDIterator import IDIterator
from Chapter5.ID.IDGenerator import id_generator


def main():
    """
    Main function to prompt the user for an ID and choice between an iterator or generator.
    It will then use the selected method to generate and print the next 10 valid IDs.

    :return: None
    """
    input_id = int(input("Enter ID: "))  # Prompt the user to enter an initial ID
    type_of = input("Generator or Iterator? (gen/it)? ")  # Prompt the user to choose between generator or iterator

    if type_of == "it":
        # If the user chooses iterator
        it = IDIterator(input_id)  # Create an instance of IDIterator
        it_id = iter(it)  # Get the iterator from the instance
        for _ in range(10):
            print(next(it_id))  # Print the next 10 IDs using the iterator
    elif type_of == "gen":
        # If the user chooses generator
        gen_id = id_generator(input_id)  # Create an ID generator
        for _ in range(10):
            print(next(gen_id))  # Print the next 10 IDs using the generator


if __name__ == "__main__":
    main()
