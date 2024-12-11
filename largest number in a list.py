def find_largest_number(numbers):
    # Check if the list is empty
    if not numbers:
        return None  # Return None for an empty list
    
    # Initialize the largest number as the first element
    largest = numbers[0]
    
    # Iterate through the list
    for number in numbers:
        # Update largest if a larger number is found
        if number > largest:
            largest = number
    
    return largest

# Example usage
numbers = [10, 25, 47, 3, 98, 56, 12]
largest_number = find_largest_number(numbers)
if largest_number is not None:
    print(f"The largest number in the list is: {largest_number}")
else:
    print("The list is empty.")
