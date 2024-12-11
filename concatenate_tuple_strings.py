def concatenate_tuple_strings(tpl):
    result = ""
    for item in tpl:
        result += item  # Concatenate each string to the result
    return result

# Example usage
my_tuple = ("Hello", " ", "World", "!")
concatenated_string = concatenate_tuple_strings(my_tuple)

print(f"The tuple is: {my_tuple}")
print(f"The concatenated string is: '{concatenated_string}'")
