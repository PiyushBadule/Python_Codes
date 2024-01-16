def to_binary(number):
    """
    Converts an integer to its binary representation.

    Args:
    number (int): The number to be converted.

    Returns:
    str: Binary representation of the number.
    """
    return "{0:b}".format(number)

def binary_addition(binary1, binary2):
    """
    Performs binary addition of two binary strings.

    Args:
    binary1 (str): The first binary number as a string.
    binary2 (str): The second binary number as a string.

    Returns:
    str: The result of binary addition.
    """
    return bin(int(binary1, 2) + int(binary2, 2))[2:]

def main():
    """
    Main function to drive the program. It converts two integers to their binary 
    representations and then performs binary addition.
    """
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))

        first_binary = to_binary(first_number)
        second_binary = to_binary(second_number)

        result = binary_addition(first_binary, second_binary)
        print("Binary Addition Result:", result)
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
