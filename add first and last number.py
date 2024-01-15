def add_first_last_digit(number):
    """
    Add the first and last digits of a given number.

    Parameters:
    number (int): The number whose first and last digits will be added.

    Returns:
    int: The sum of the first and last digits of the number.
    """

    # Extract the last digit
    last_digit = number % 10

    # Extract the first digit
    while number >= 10:
        number //= 10
    first_digit = number

    # Calculate the result
    result = first_digit + last_digit

    return result


def main():
    """
    Main function to execute the program.
    """
    try:
        number = int(input("Enter a Number: "))
        sum_of_digits = add_first_last_digit(number)
        print("The Sum is:", sum_of_digits)
    except ValueError:
        print("Please enter a valid integer.")


# Execute the main function when the script is run
if __name__ == "__main__":
    main()
