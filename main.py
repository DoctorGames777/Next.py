import sys
import os
import importlib.util


def validate_input(input_value):
    """
    Validate the user input to ensure it is a number between 1 and 6.

    :param input_value: The input value to validate, expected to be a string.
    :return: The validated input as an integer.
    :raises ValueError: If the input is not a number or not in the range 1 to 6.
    """
    try:
        # Try to convert the input to an integer
        user_input = int(input_value)
    except ValueError:
        # Raise an error if conversion fails
        raise ValueError("Invalid input. Please enter a number between 1 and 6.")

    # Check if the number is in the valid range
    if 1 <= user_input <= 6:
        return user_input
    else:
        # Raise an error if the number is out of range
        raise ValueError("Input must be between 1 and 6.")


def get_input():
    """
    Prompt the user to enter a number between 1 and 6 and validate it.

    :return: The validated input as an integer.
    """
    while True:
        try:
            # Prompt the user for input
            user_input = input("Enter a number between 1 and 6: ")
            # Validate the input
            return validate_input(user_input)
        except ValueError as e:
            # Print an error message if validation fails
            print(f"Error: {e}")


def load_and_run_module(module_name):
    """
    Load and run a specified module by its name. The module should have a main function.

    :param module_name: The name of the module to load and run.
    :return: None
    """
    try:
        # Find the module specification
        spec = importlib.util.find_spec(module_name)
        if spec is None:
            # Print an error if the module is not found
            print(f"Module {module_name} not found")
            return

        # Create a module from the specification
        module = importlib.util.module_from_spec(spec)
        # Add the module to sys.modules
        sys.modules[module_name] = module
        # Execute the module
        spec.loader.exec_module(module)

        # Call the main function of the module if it exists
        if hasattr(module, 'main'):
            module.main()
        else:
            # Print an error if the main function is not found
            print(f"Module {module_name} does not have a main() function")
    except Exception as e:
        # Print an error if the module fails to load or run
        print(f"Failed to load module {module_name}: {e}")


def main():
    """
    Main function to handle input and load the appropriate module.

    :return: None
    """
    if len(sys.argv) == 2:
        try:
            # Validate the command line input
            user_input = validate_input(sys.argv[1])
        except ValueError as e:
            # Print an error message if validation fails
            print(f"Error: {e}")
            sys.exit(1)
    else:
        # Get and validate input from the user
        user_input = get_input()

    # Add project root to sys.path
    project_root = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, project_root)

    # Use a dictionary to map user input to module names
    chapter_modules = {
        1: 'Chapter1.one_liners',
        2: 'Chapter2.object_oriented_programming',
        3: 'Chapter3.exceptions',
        4: 'Chapter4.generators',
        5: 'Chapter5.iterators',
        6: 'Chapter6.modules'
    }

    # Get the module name based on user input
    module_name = chapter_modules.get(user_input)
    if module_name:
        # Load and run the specified module
        load_and_run_module(module_name)
    else:
        # Print an error if no module is found for the input
        print(f"No module found for input {user_input}")


if __name__ == "__main__":
    main()
