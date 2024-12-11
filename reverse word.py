def reverse_words(sentence):
    """
    Reverse each word in the sentence while keeping their original order.
    """
    # Split the sentence into words, reverse each word, and join them back into a sentence
    reversed_words = ' '.join(word[::-1] for word in sentence.split())
    return reversed_words

# Example usage
sentence = input("Enter a sentence: ")
reversed_sentence = reverse_words(sentence)

print(f"Sentence with reversed words: {reversed_sentence}")
