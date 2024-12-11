def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.
    The Fibonacci sequence is defined as:
    F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
n = int(input("Enter the position of the Fibonacci number to calculate (n >= 0): "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
