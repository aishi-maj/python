def count_vowels(string):
    """
    Count the number of vowels in the given string.
    Vowels are 'a', 'e', 'i', 'o', 'u' (case-insensitive).
    """
    vowels = "aeiou"
    # Convert the string to lowercase and count the vowels
    return sum(1 for char in string.lower() if char in vowels)

# Example usage
input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)

print(f"The number of vowels in '{input_string}' is: {vowel_count}")
