from array import array

def array_operations():
    # Create an array of integers
    values = array('i', [5, 4, 3, 2, 1])

    # Reverse the array
    values.reverse()
    print("Reversed array:", values)

    # Additional array operations

    # Append a new element to the array
    values.append(6)
    print("After appending 6:", values)

    # Remove an element from the array
    values.remove(2)
    print("After removing 2:", values)

    # Insert an element at a specific position
    values.insert(2, 8)
    print("After inserting 8 at position 2:", values)

    # Access elements through iteration
    print("All elements:")
    for value in values:
        print(value)

    # Find the index of an element
    index_of_three = values.index(3)
    print("Index of 3:", index_of_three)

    # Update an element at a specific position
    values[0] = 7
    print("After updating the first element to 7:", values)

    # Slicing the array
    sliced_array = values[1:4]
    print("Sliced array (elements 1 to 3):", sliced_array)

if __name__ == "__main__":
    array_operations()
