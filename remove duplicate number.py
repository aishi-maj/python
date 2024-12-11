def remove_duplicates(items):
    # Create an empty set to track seen elements
    seen = set()
    # Use a list comprehension to filter out duplicates
    result = [item for item in items if not (item in seen or seen.add(item))]
    return result

# Example usage
original_list = [10, 20, 10, 30, 20, 40, 30, 50]
unique_list = remove_duplicates(original_list)
print(f"Original list: {original_list}")
print(f"List after removing duplicates: {unique_list}")
