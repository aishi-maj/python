def check_element_in_tuple(tpl, element):
    # Use the 'in' keyword to check for element existence
    return element in tpl

# Example usage
my_tuple = (10, 20, 30, 40, 50)
element_to_check = 30

if check_element_in_tuple(my_tuple, element_to_check):
    print(f"The element {element_to_check} exists in the tuple.")
else:
    print(f"The element {element_to_check} does not exist in the tuple.")
