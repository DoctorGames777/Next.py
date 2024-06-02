import functools
import os


def main():
    """
    Main function to execute different sections of a task based on user input.

    This function reads names from a file and performs different operations based on the user's choice:
    1. Print the longest name.
    2. Print the total number of characters in all names.
    3. Print the shortest name(s).
    4. Write the length of each name to a new file.
    5. Print names of a specific length provided by the user.

    :return: None
    """
    # Get the absolute path to the directory containing the script
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    # Open the file containing names
    with open(os.path.join(__location__, "names.txt"), 'r') as file_of_names:
        # Prompt the user to choose a section to run
        match input("Which section of the question do you want to run (1/2/3/4/5)? "):
            case "1":
                # Section 1: Print the longest name
                print(max(file_of_names.read().split('\n'), key=len))
            case "2":
                # Section 2: Print the total number of characters in all names
                print(sum([len(name) for name in file_of_names.read().split('\n')]))
            case "3":
                # Section 3: Print the shortest name(s)
                list_of_names = file_of_names.read().split('\n')
                list_of_names_len = [len(name) for name in list_of_names]
                min_len = functools.reduce(min, list_of_names_len)
                print(''.join([name + '\n' if len(name) == min_len else '' for name in list_of_names]).rstrip())
            case "4":
                # Section 4: Write the length of each name to a new file
                with open(os.path.join(__location__, "name_length.txt"), 'w') as file_of_names_len:
                    file_of_names_len.write(
                        "".join([str(name_len) + '\n' for name_len in [len(name) for name in file_of_names.read().split('\n')]]).rstrip()
                    )
            case "5":
                # Section 5: Print names of a specific length provided by the user
                len_input = int(input("Enter name length: "))
                print(''.join([name + '\n' if len(name) == len_input else '' for name in file_of_names.read().split('\n')]).rstrip())
            case _:
                # Default case: Handle invalid input
                print("There is no such section in the question.")


if __name__ == "__main__":
    main()
