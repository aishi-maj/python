def is_palindrome(string):
    """
    Check if the given string is a palindrome.
    A string is a palindrome if it reads the same backward as forward.
    """
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    # Check if the string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage
input_string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
