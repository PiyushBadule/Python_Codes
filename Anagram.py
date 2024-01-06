def check_anagram(input_string):
    # Split the input string into two parts
    words = input_string.split(" ")

    # Ensure that there are exactly two words to compare
    if len(words) != 2:
        return "Invalid Input"

    # Extract the words
    first_word, second_word = words

    # Sort the characters of each word and compare
    if sorted(first_word) == sorted(second_word):
        return "Anagram"
    else:
        return "Not Anagram"

# Input string
input_string = 'listen silent'

# Check if the words are anagrams and print the result
result = check_anagram(input_string)
print(result)
