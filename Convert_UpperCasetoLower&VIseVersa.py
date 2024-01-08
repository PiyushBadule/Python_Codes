def toggle_case(input_string):
    """
    Takes an input string and returns a new string with the case of each alphabetical character toggled.

    Args:
    input_string (str): The string to be modified.

    Returns:
    str: A new string with all alphabetical characters having their case toggled from the original.

    Example:
    >>> toggle_case("Hello World")
    'hELLO wORLD'
    """
    new_string = ''
    for char in input_string:
        if char.isupper():
            new_string += char.lower()
        elif char.islower():
            new_string += char.upper()
        else:
            new_string += char
    return new_string

def main():
    """
    Main function to execute script tasks.
    """
    # User input
    input_string = input("Enter the string: ")
    # Manipulate and print the new string
    print(toggle_case(input_string))

if __name__ == "__main__":
    main()
