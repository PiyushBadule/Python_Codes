# Write a function which takes a list as a argument and double the each from that list.
# output:- ["aa", "bb", "cc"]

def double_elements(elements):
    """
    Doubles each element in the given list.

    Args:
    elements (list): A list of elements (strings or other types) to be doubled.

    Returns:
    list: A new list with each element from the input list doubled.
    """
    doubled_list = [element * 2 for element in elements]
    return doubled_list

def main():
    """
    Main function to execute the program.
    """
    input_list = ["a", "b", "c"]
    result = double_elements(input_list)
    print(result)

if __name__ == "__main__":
    main()
