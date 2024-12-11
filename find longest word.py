def find_longest_word(sentence):
    """
    Find the longest word in the given sentence.
    """
    # Split the sentence into words
    words = sentence.split()
    
    # Find the longest word by length
    longest_word = max(words, key=len)
    
    return longest_word

# Example usage
sentence = input("Enter a sentence: ")
longest_word = find_longest_word(sentence)

print(f"The longest word in the sentence is: {longest_word}")
