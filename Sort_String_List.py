# Sort the string list on the basis of length
def sort_words_by_length(word_list):
    """
    Sorts a list of words based on their length.

    Args:
    word_list (list): A list of words (strings) to be sorted.

    Returns:
    list: A list of words sorted by their length.
    """
    try:
        sorted_list = sorted(word_list, key=len)
        return sorted_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    """
    Main function that sorts a predefined list of words by their length.
    """
    words = ["cat", "bag", "at", "laptop", "zoo"]

    sorted_words = sort_words_by_length(words)
    print(sorted_words)

if __name__ == "__main__":
    main()


