# Enter the first number: 54
# Enter the second number: 24
# The H.C.F. of 54 and 24 is 6

def compute_hcf(x, y):
    """
    Calculate the Highest Common Factor (HCF) or Greatest Common Divisor (GCD) of two numbers.

    Args:
    x (int): The first number.
    y (int): The second number.

    Returns:
    int: The HCF or GCD of the two numbers.
    """
    while(y):
        x, y = y, x % y
    return x

def main():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        hcf = compute_hcf(num1, num2)
        print(f"The H.C.F. of {num1} and {num2} is {hcf}")
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
