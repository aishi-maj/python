def find_numbers():
    for number in range(100, 201):
        if number % 5 == 0 and number % 3 != 0:
            print(number)

# Run the function to print the numbers
find_numbers()
