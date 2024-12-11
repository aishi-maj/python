# Define the original dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}

# Invert the dictionary (keys become values, values become keys)
inverted_dict = {value: key for key, value in original_dict.items()}

# Print the inverted dictionary
print("Original Dictionary:", original_dict)
print("Inverted Dictionary:", inverted_dict)
