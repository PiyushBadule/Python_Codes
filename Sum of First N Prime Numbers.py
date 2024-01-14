# Program to Print Sum of First n Number of Prime Numbers
def is_prime(number):
    """
    Determines if a number is a prime number.

    Args:
    number (int): The number to be checked for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        return True
    else:
        return False

def calculate_sum_of_first_n_primes(n):
    """
    Calculates the sum of the first 'n' prime numbers.

    Args:
    n (int): The number of prime numbers to sum.

    Returns:
    int: The sum of the first 'n' prime numbers.
    """
    count = 0
    sum_primes = 0
    number = 2

    while count < n:
        if is_prime(number):
            sum_primes += number
            count += 1
        number += 1

    return sum_primes

def main():
    """
    Main function to calculate the sum of the first 'n' prime numbers.
    """
    num_primes = int(input("Enter the number of prime numbers you want the sum of: "))
    sum_of_primes = calculate_sum_of_first_n_primes(num_primes)
    print("Sum of the first", num_primes, "prime numbers:", sum_of_primes)

if __name__ == "__main__":
    main()
