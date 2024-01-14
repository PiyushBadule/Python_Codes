# input:- "I am Piyush"
# output:-  hsuyiP ma I
def reverse_string(input_string):
    """
    Reverses the given string.

    Args:
    input_string (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    return input_string[::-1]

def main():
    """
    Main function to demonstrate string reversal.
    """
    original_string = "I am Piyush"
    reversed_string = reverse_string(original_string)
    print("Reversed String:", reversed_string)

if __name__ == "__main__":
    main()
