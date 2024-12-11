# Get input from the user
input_string = input("Enter a string: ")

# Initialize an empty dictionary to store character counts
char_count = {}

# Iterate through each character in the string
for char in input_string:
    # Increment the count for the character or initialize it to 1
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print the character counts
print("Character occurrences:")
for char, count in char_count.items():
    print(f"'{char}': {count}")
