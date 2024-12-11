def are_anagrams(str1, str2):
    """
    Check if two strings are anagrams of each other.
    Anagrams are words that have the same characters, but in a different order.
    """
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)

# Example usage
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
