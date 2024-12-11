def sum_of_odds(n):
    # Initialize sum variable
    total_sum = 0
    # Loop through all numbers from 1 to n
    for i in range(1, n+1):
        if i % 2 != 0:  # Check if the number is odd
            total_sum += i
    return total_sum

# Example usage:
n = int(input("Enter a number: "))
result = sum_of_odds(n)
print(f"The sum of all odd numbers up to {n} is: {result}")
