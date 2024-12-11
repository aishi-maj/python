def replace_substring(original_string, old_substring, new_substring):
    """
    Replace all occurrences of 'old_substring' in 'original_string' with 'new_substring'.
    """
    return original_string.replace(old_substring, new_substring)

# Example usage
original_string = input("Enter the original string: ")
old_substring = input("Enter the substring to replace: ")
new_substring = input("Enter the new substring: ")

# Replace the substring and print the result
result_string = replace_substring(original_string, old_substring, new_substring)
print(f"Updated string: {result_string}")
