# input:-  " I am Piyush"
# output:- Piyush am I
def reverse_word_order(input_string):
    """
    Reverses the order of words in the given string.

    This function keeps the characters of each word intact but reverses the order of the words in the string.

    Args:
    input_string (str): The string whose word order is to be reversed.

    Returns:
    str: A string with the word order reversed.
    """
    reversed_word_order = []
    word = ''
    for char in input_string[::-1]:
        if char == " ":
            reversed_word_order.append(word)
            word = ""
        else:
            word += char
    reversed_word_order.append(word)  # Append the last word

    return ' '.join(reversed_word_order[::-1])

def main():
    """
    Main function to demonstrate the reversal of word order in a string.
    """
    input_string = "I am Piyush"
    result = reverse_word_order(input_string)
    print("Result:", result)

if __name__ == "__main__":
    main()
