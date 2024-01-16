def generate_multiplication_table(number):
    """
    Generates and prints the multiplication table for the given number.

    Args:
    number (int): The number for which the multiplication table is generated.

    Returns:
    None
    """
    for x in range(1, 11):
        print(f'{number} * {x} = {number * x}')

def main():
    """
    Main function to drive the program. It takes user input and generates
    the multiplication table for the input number.
    """
    try:
        number = int(input("Enter Number: "))
        generate_multiplication_table(number)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
