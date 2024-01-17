def decimal_to_binary(number):
    """
    Convert a decimal number to its binary representation.

    Parameters:
    number (int): A decimal number.

    Returns:
    str: Binary representation of the decimal number.
    """
    return "{0:b}".format(number)

def main():
    """
    Main function that prompts the user to enter a decimal number and prints its binary representation.
    """
    try:
        decimal_number = int(input("Enter Number: "))
        binary_representation = decimal_to_binary(decimal_number)
        print(binary_representation)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
