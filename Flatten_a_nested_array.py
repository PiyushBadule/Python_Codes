def flatten(nested_list):
    """
    Flatten a nested list of lists into a single list.

    Args:
    nested_list (list): A list which can contain elements and/or other lists.

    Returns:
    list: A single, flat list with all the elements of the nested lists.
    """
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            # If the element is a list, extend the flat list with the flattened element
            flat_list.extend(flatten(element))
        else:
            # If the element is not a list, append it to the flat list
            flat_list.append(element)
    return flat_list

# Testing the function with an example
if __name__ == "__main__":
    nested_list = [1, 2, [3], [[4]], [[[5]]]]
    print("Original list:", nested_list)
    print("Flattened list:", flatten(nested_list))


