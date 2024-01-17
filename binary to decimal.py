def binary_to_decimal(binary_string):
    """
    Convert a binary number (given as a string) to its decimal equivalent.

    Parameters:
    binary_string (str): A string representing a binary number.

    Returns:
    int: Decimal equivalent of the binary number.
    """
    try:
        decimal_number = int(binary_string, 2)
    except ValueError:
        return "Invalid binary number"
    return decimal_number

def main():
    """
    Main function to take user input for binary number and print its decimal equivalent.
    """
    binary_number = input('Enter the binary number: ')
    decimal_number = binary_to_decimal(binary_number)
    print(decimal_number)

if __name__ == "__main__":
    main()
