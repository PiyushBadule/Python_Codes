#Returns true if x is a power - of - 10.
# Otherwise returns false.
# INPUT:
# Input1: 3
# Output1: false
# Input1: 10
# Output1: true


import math

def is_power_of_ten(number):
    """
    Check if the given number is a power of 10.

    Args:
    number (int): The number to check.

    Returns:
    bool: True if the number is a power of 10, False otherwise.
    """
    if number <= 0:
        return False

    # Calculate the logarithm base 10 and round it to the nearest integer
    logarithm = math.log(number, 10)
    nearest_integer = round(logarithm)

    # Check if 10 raised to the power of this integer equals the original number
    return 10 ** nearest_integer == number

def main():
    """
    Main function to execute the program.
    """
    try:
        input_number = int(input("Enter a number: "))
        result = is_power_of_ten(input_number)
        print(result)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
