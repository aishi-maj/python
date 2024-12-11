def find_index_in_tuple(tpl, element):
    try:
        # Use the index() method to find the index of the element
        return tpl.index(element)
    except ValueError:
        # Handle the case where the element is not in the tuple
        return None

# Example usage
my_tuple = (10, 20, 30, 40, 50)
element_to_find = 30

index = find_index_in_tuple(my_tuple, element_to_find)

if index is not None:
    print(f"The index of {element_to_find} in the tuple is: {index}")
else:
    print(f"The element {element_to_find} is not in the tuple.")
