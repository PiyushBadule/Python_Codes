# Method 1: Iterative Approach
def is_armstrong_number(number):
    """
    Checks if the given number is an Armstrong number.
    An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
    
    :param number: int, the number to check
    :return: bool, True if the number is an Armstrong number, else False
    """
    # Convert the number to string for iteration
    str_num = str(number)
    num_length = len(str_num)
    total = 0

    # Calculate the sum of digits raised to the power of the number's length
    for digit in str_num:
        total += int(digit) ** num_length

    # Check if the calculated sum is equal to the original number
    return total == number

# Example usage:
num = 153
print(f"{num} is an Armstrong number: {is_armstrong_number(num)}")

# Method 2: Functional Approach
def is_armstrong_number(number):
    """
    Checks if the given number is an Armstrong number using a functional approach.
    An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
    
    :param number: int, the number to check
    :return: bool, True if the number is an Armstrong number, else False
    """
    # Convert the number to a list of its digits
    digits = list(map(int, str(number)))
    num_length = len(digits)
    
    # Calculate the sum of digits raised to the power of the number's length
    total = sum(map(lambda x: x ** num_length, digits))

    # Check if the calculated sum is equal to the original number
    return total == number

# Prompting user input and example usage:
try:
    num = int(input("Enter the number: "))
    result = "is" if is_armstrong_number(num) else "is not"
    print(f"{num} {result} an Armstrong number.")
except ValueError:
    print("Please enter a valid integer.")
