def rotate_list(lst, n):
    # Normalize n to handle cases where n > len(lst) or n is negative
    n = n % len(lst)
    # Rotate the list using slicing
    return lst[-n:] + lst[:-n]

# Example usage
original_list = [1, 2, 3, 4, 5, 6]
print(f"Original list: {original_list}")

# Get user input for rotation
n = int(input("Enter the number of positions to rotate: "))
rotated_list = rotate_list(original_list, n)

print(f"List after rotating by {n} positions: {rotated_list}")
