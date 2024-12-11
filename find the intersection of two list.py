def find_intersection(list1, list2):
    # Use a set to store unique elements and find common items
    return [item for item in list1 if item in list2]

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersection = find_intersection(list1, list2)

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Intersection: {intersection}")
