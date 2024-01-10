def fibonacci_sequence():
    """
    Generate an infinite Fibonacci sequence.

    Yields:
        int: The next number in the Fibonacci sequence.
    """
    first, second = 0, 1
    while True:
        yield first
        first, second = second, first + second


def main():
    """
    Main function to print Fibonacci numbers up to a specified limit (10 in this case).
    """
    print("Fibonacci series up to 10:")
    for number in fibonacci_sequence():
        if number > 10:
            break
        print(number, end=" ")


if __name__ == "__main__":
    main()
