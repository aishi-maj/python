def count_words(string):
    """
    Count the number of words in a string.
    A word is defined as a sequence of characters separated by spaces.
    """
    # Split the string by spaces and count the length of the resulting list
    words = string.split()
    return len(words)

# Example usage
input_string = input("Enter a string: ")
word_count = count_words(input_string)

print(f"The number of words in the string is: {word_count}")
