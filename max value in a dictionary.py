# Define a dictionary
sample_dict = {'a': 10, 'b': 25, 'c': 8, 'd': 42}

# Find the key with the maximum value
max_key = max(sample_dict, key=sample_dict.get)

# Print the result
print("Key with the maximum value:", max_key)
print("Maximum value:", sample_dict[max_key])
