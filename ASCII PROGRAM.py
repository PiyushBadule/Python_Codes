def ascii_addition():
    """
    This function takes two single characters as input from the user,
    converts them to their ASCII values, and prints the sum of those ASCII values.
    """
    try:
        # Prompt the user for the first character and get its ASCII value
        char1 = input("Enter the first character: ")
        if len(char1) != 1:
            raise ValueError("Please enter only one character.")
        ascii_val1 = ord(char1)

        # Prompt the user for the second character and get its ASCII value
        char2 = input("Enter the second character: ")
        if len(char2) != 1:
            raise ValueError("Please enter only one character.")
        ascii_val2 = ord(char2)

        # Calculate and print the sum of the ASCII values
        ascii_sum = ascii_val1 + ascii_val2
        print(f"The sum of the ASCII values of '{char1}' and '{char2}' is: {ascii_sum}")

    except ValueError as e:
        # Handle the exception if the user inputs more than one character
        print(e)

if __name__ == "__main__":
    ascii_addition()
