def print_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print(' ' * (n - i), end='')
        # Print stars
        print('*' * (2 * i - 1))

# Example usage:
n = int(input("Enter the number of levels for the pyramid: "))
print_pyramid(n)
