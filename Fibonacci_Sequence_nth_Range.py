def fibonacci_up_to_n(n):
    """
    Generate a Fibonacci sequence up to a specified limit.

    Args:
    n (int): The upper limit of the Fibonacci sequence to generate.

    Yields:
    int: The next number in the Fibonacci sequence up to n.
    """
    first, second = 0, 1
    while first <= n:
        yield first
        first, second = second, first + second


def main():
    """
    Main function to prompt user for the range and print the Fibonacci sequence up to that range.
    """
    nterms = int(input("Enter The Range Of Sequence:"))

    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence up to", nterms, "is:")
        print(0)
    else:
        print("Fibonacci sequence up to", nterms, "is:")
        for number in fibonacci_up_to_n(nterms):
            print(number, end=", ")


if __name__ == "__main__":
    main()
