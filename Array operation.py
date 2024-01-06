from array import array

def main():
    # Create an array of integers
    numbers = array('i', [1, 2, 3, 4, 5])

    # Print the second element (index 1)
    print("Second element:", numbers[1])

    # Additional array operations

    # Append a new element to the array
    numbers.append(6)
    print("After appending 6:", numbers)

    # Remove an element from the array
    numbers.remove(3)
    print("After removing 3:", numbers)

    # Insert an element at a specific position
    numbers.insert(2, 9)
    print("After inserting 9 at position 2:", numbers)

    # Access elements through iteration
    print("All elements:")
    for num in numbers:
        print(num)

    # Find the index of an element
    index_of_five = numbers.index(5)
    print("Index of 5:", index_of_five)

    # Reverse the array
    numbers.reverse()
    print("Reversed array:", numbers)

if __name__ == "__main__":
    main()
