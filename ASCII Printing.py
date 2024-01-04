def ascii_of_input(user_input):
    """
    This function takes a string and returns a dictionary with characters as keys
    and their corresponding ASCII values as values.

    :param user_input: str - the string for which ASCII values are required
    :return: dict - a dictionary of characters and their ASCII values
    """
    return {char: ord(char) for char in user_input}


def main():
    """
    Main function to take user input and print the ASCII values of each character.
    """
    try:
        # Taking input from the user
        user_input = input("Enter a string to get its ASCII values: ")
        
        # Getting ASCII values through the function
        ascii_values = ascii_of_input(user_input)
        
        # Printing the ASCII values
        print("\nASCII values:")
        for char, ascii_val in ascii_values.items():
            print(f"'{char}': {ascii_val}")

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
