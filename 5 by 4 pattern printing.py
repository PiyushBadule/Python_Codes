def print_pattern(rows, columns, symbol):
    """
    Prints a rectangular pattern of a specified size and symbol.

    Parameters:
    rows (int): The number of rows in the pattern.
    columns (int): The number of columns in the pattern.
    symbol (str): The symbol to be used in the pattern.
    """
    for _ in range(rows):
        # Print the specified symbol 'columns' times, followed by a space, in one line
        print(symbol * columns)


def main():
    """
    Main function to define pattern parameters and call the print_pattern function.
    """
    # Define the size of the pattern
    rows = 4
    columns = 5
    symbol = "# "

    # Print the pattern
    print_pattern(rows, columns, symbol)


# Standard boilerplate to call the main() function
if __name__ == '__main__':
    main()
