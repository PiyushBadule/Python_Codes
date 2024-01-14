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

def calculate_sum_of_primes(upper_limit):
    """
    Calculates the sum of all prime numbers up to a given limit.

    Args:
    upper_limit (int): The upper limit up to which prime numbers are considered.

    Returns:
    tuple: A tuple containing the sum of prime numbers and the list of these primes.
    """
    primes = [num for num in range(2, upper_limit + 1) if is_prime(num)]
    return sum(primes), primes

def main():
    """
    Main function to calculate the sum of prime numbers up to a user-defined number.
    """
    upper_limit = int(input("Enter a number: "))
    prime_sum, prime_list = calculate_sum_of_primes(upper_limit)
    print("Sum of prime numbers:", prime_sum)
    print("List of prime numbers:", prime_list)

if __name__ == "__main__":
    main()
