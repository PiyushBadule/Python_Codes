def pop_list_based_on_lowest(input_list):
    """
    Continuously pops and prints the lowest element from the input list until the list is empty.

    Args:
    input_list (list): A list of numeric elements.

    Returns:
    None: The function prints the lowest element each time one is popped, but does not return anything.
    """
    while input_list:
        max_element = min(input_list)
        input_list.remove(max_element)
        print(max_element)

if __name__ == "__main__":
    a = [10, 50, 30, 100, 20, 5, 20]
    pop_list_based_on_lowest(a)
