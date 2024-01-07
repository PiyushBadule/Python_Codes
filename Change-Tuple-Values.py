def change_tuple_value(original_tuple, index, new_value):
    """
    Changes a value in a tuple.

    Tuples are immutable, so this function converts the tuple to a list, changes the value at the specified index,
    and then converts it back to a tuple.

    Parameters:
    original_tuple (tuple): The original tuple.
    index (int): The index of the element to replace.
    new_value (any): The new value to insert at the specified index.

    Returns:
    tuple: The new tuple with the changed value.
    """

    temp_list = list(original_tuple)  # Convert tuple to list
    temp_list[index] = new_value      # Change the value at the specified index
    return tuple(temp_list)           # Convert list back to tuple and return


def main():
    """
    Main function to execute the script functionality.
    Initializes a tuple, changes a value, and prints the result.
    """

    x = ("apple", "banana", "cherry")  # Original tuple
    index_to_change = 1                # Index of the value to change
    new_value = "kiwi"                 # New value to insert

    # Change the tuple value and use the same variable name for the new tuple
    x = change_tuple_value(x, index_to_change, new_value)

    print(x)  # Print the new tuple


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
