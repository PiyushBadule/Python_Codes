# "Write a Python program that takes an integer N as input, followed by N integers. 
# The program should calculate and output the sum of the maximum and minimum numbers from the provided list of integers.
# Ensure your code is properly structured, includes docstrings, and handles cases where the input might not be as expected."

def solution(numbers):
    """
    Calculate the sum of the maximum and minimum values in a list.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    int: The sum of the maximum and minimum integers in the list.
    """
    max_value = max(numbers)
    min_value = min(numbers)
    return max_value + min_value


def main():
    """
    Main function to execute the program.
    Takes user input for the number of elements and the elements themselves,
    then prints the sum of the maximum and minimum values in the list.
    """
    try:
        N = int(input("Enter the number of elements: "))
        print("Now enter", N, "numbers separated by space:")
        elements = list(map(int, input().split()))

        if len(elements) != N:
            print("Please input exactly {0} elements".format(N))
        else:
            print("The sum of the maximum and minimum numbers is:", solution(elements))

    except ValueError:
        print("Please enter valid integers.")


if __name__ == "__main__":
    main()
