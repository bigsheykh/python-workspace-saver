# Can you create a Python file that doesn't have inputs and only has outputs?
# Additionally, can it be longer than 50 lines?
# Also, can it have imports and use those imports?
# Also, can it use "binascii.a2b_uu" function?

import binascii

# Define a string
simple_string = "SGVsbG8sIFB5dGh"

# Encoded string using the binascii.b2a_hqx function
coded_bytes = binascii.b2a_hqx(simple_string.encode())
print(coded_bytes)

# Decode the string using the binascii.a2b_hqx function
decoded_bytes = binascii.a2b_hqx(coded_bytes)
print(decoded_bytes)

# Convert the decoded bytes to a string
decoded_string = decoded_bytes[0].decode()

# Print the decoded string
print("Decoded String:", decoded_string)

# Perform some calculations
a = 10
b = 20
c = a + b

# Print the result
print("Result of the calculation:", c)

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers
sum_of_numbers = sum(numbers)

# Print the sum
print("Sum of the numbers:", sum_of_numbers)

# Generate a Fibonacci sequence
fibonacci = [0, 1]
limit = 10

while len(fibonacci) < limit:
    next_number = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_number)

# Print the Fibonacci sequence
print("Fibonacci sequence:", fibonacci)

# Define a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Print the dictionary
print("Person details:", person)

# Perform some string operations
text = "Hello, World!"

# Check if the string starts with "Hello"
if text.startswith("Hello"):
    print("The string starts with 'Hello'")
else:
    print("The string does not start with 'Hello'")

# Count the occurrences of the letter 'o' in the string
count = text.count('o')

# Print the count
print("Count of 'o':", count)

# Create a formatted string
formatted_string = f"The sum of {a} and {b} is {c}"

# Print the formatted string
print("Formatted string:", formatted_string)


T='Hiya'
val=[1,2,3]

