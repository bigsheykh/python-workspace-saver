# This is an example Python file with outputs and imports

import random
import math

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Calculate the square root of the random number
square_root = math.sqrt(random_number)

# Print the random number and its square root
print(f"Random number: {random_number}")
print(f"Square root of the random number: {square_root}")

# Generate a list of 10 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(10)]

# Print the list of random numbers
print("\nRandom numbers:")
for num in random_numbers:
    print(num)

# Calculate the sum of the random numbers
sum_of_numbers = sum(random_numbers)

# Print the sum of the random numbers
print(f"\nSum of random numbers: {sum_of_numbers}")

# Calculate the average of the random numbers
average = sum_of_numbers / len(random_numbers)

# Print the average of the random numbers
print(f"Average of random numbers: {average}")

# Output a final message
print("\nPython file execution complete. Outputs generated.")
