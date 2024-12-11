def factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Get input from the user
number = int(input("Enter a number to calculate its factorial: "))

# Calculate and print the factorial
print(f"The factorial of {number} is: {factorial(number)}")
