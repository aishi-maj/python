def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_primes(numbers):
    """Return a list of prime numbers from the given list."""
    return [num for num in numbers if is_prime(num)]

# Example usage
numbers_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]
prime_numbers = filter_primes(numbers_list)

print("Original List:", numbers_list)
print("Prime Numbers:", prime_numbers)
