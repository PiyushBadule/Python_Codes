# input:- "I am Piyush"
# output:- I ma hsuyiP
def reverse_each_word(input_string):
    """
    Reverses each word in the given string.

    This function keeps the word order intact but reverses the characters in each word.

    Args:
    input_string (str): The string whose words are to be reversed.

    Returns:
    str: A string with each word reversed.
    """
    reversed_words = []
    word = ''
    for char in input_string:
        if char == " ":
            reversed_words.append(word[::-1])
            word = ""
        else:
            word += char
    reversed_words.append(word[::-1])  # Append the last word

    return ' '.join(reversed_words)

def main():
    """
    Main function to demonstrate the reversal of each word in a string.
    """
    input_string = "I am Piyush"
    result = reverse_each_word(input_string)
    print("Result:", result)

if __name__ == "__main__":
    main()
