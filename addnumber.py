def sum_of_digits(number):
    """
    Calculates and returns the sum of the digits of the given number.

    Args:
    number (int): The number whose digits are to be summed.

    Returns:
    int: The sum of the digits.
    """
    total_sum = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        total_sum += digit

    return total_sum

def main():
    """
    Main function to drive the program. It takes user input and calculates
    the sum of digits of the input number.
    """
    try:
        number = int(input("Enter Number: "))
        result = sum_of_digits(number)
        print("The Sum Is:", result)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
