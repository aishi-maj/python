def get_even_numbers(numbers):
    # Create a new list to store even numbers
    even_numbers = []
    
    # Iterate through the given list
    for number in numbers:
        # Check if the number is even
        if number % 2 == 0:
            even_numbers.append(number)
    
    return even_numbers

# Example usage
numbers = [10, 15, 23, 42, 56, 73, 88]
even_numbers = get_even_numbers(numbers)
print(f"The even numbers in the list are: {even_numbers}")
