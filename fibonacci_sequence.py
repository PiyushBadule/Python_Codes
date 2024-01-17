def fibonacci_while(n):
    """
    Generate a Fibonacci sequence up to n terms using a while loop.

    Parameters:
    n (int): Number of terms in the Fibonacci sequence to generate.

    Prints:
    The Fibonacci sequence up to n terms.
    """
    count, first, second = 1, 0, 1
    while count <= n:
        print(first, end=',')
        first, second = second, first + second
        count += 1
    print()


def fibonacci_function(n):
    """
    Calculate the nth Fibonacci number using iteration.

    Parameters:
    n (int): The position in the Fibonacci sequence.

    Returns:
    int: The nth Fibonacci number.
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def main():
    """
    Main function to demonstrate the Fibonacci sequence generation
    using two different methods.
    """
    number = int(input("Enter Number: "))
    
    print("Fibonacci sequence using while loop:")
    fibonacci_while(number)

    print("\n******************************************************************************************\n")

    print("Fibonacci sequence using function:")
    for i in range(10):
        print(fibonacci_function(i), end=',')


if __name__ == "__main__":
    main()
