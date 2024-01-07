def sort_in_ascending_order(array):
    """
    Sorts a given list of integers in ascending order.

    This function iterates through each element of the array, compares it with every other element,
    and swaps them if they are in the wrong order, effectively sorting the whole array in ascending order.

    Parameters:
    array (list of int): The list of integers to be sorted.

    Returns:
    None: The function modifies the list in place and does not return anything.

    Prints:
    - The original elements of the array.
    - The elements of the array after sorting in ascending order.
    """

    print("Elements of the original array: ")
    print(*array)  # Print original array

    # Sort the array in ascending order
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]  # Swap elements

    print("\nElements of array sorted in ascending order: ")
    print(*array)  # Print sorted array


def main():
    """
    Main function to execute the script functionality.
    Initializes an array, and sorts it in ascending order.
    """
    # Initialize array
    array = [5, 2, 8, 7, 1]

    # Call the sorting function with the array
    sort_in_ascending_order(array)


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
