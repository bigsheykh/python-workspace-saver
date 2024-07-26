import math
import random
import datetime

print("Welcome to the Python script with no inputs!")

print("Here are some random numbers:")
for i in range(10):
    print(random.randint(1, 100))

print("\nHere are some mathematical calculations:")
print("The value of pi is:", math.pi)
print("The square root of 25 is:", math.sqrt(25))
print("The sine of 45 degrees is:", math.sin(math.radians(45)))

print("\nHere's the current date and time:")
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

print("\nHere's a random joke:")
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why was the math book sad? Because of all of its problems!",
    "Why can't a bicycle stand up by itself? Because it's two-tired!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!"
]
print(random.choice(jokes))

print("\nHere's a list of the first 20 Fibonacci numbers:")
a, b = 0, 1
fibonacci_numbers = [a, b]
for i in range(18):
    a, b = b, a + b
    fibonacci_numbers.append(b)
print(fibonacci_numbers)

print("\nHere's a random binary number:")
binary_number = ''.join(random.choices(['0', '1'], k=8))
print(binary_number)

print("\nHere's the binary representation of the number 42:")
print(bin(42))

print("\nHere's a random hexadecimal number:")
hex_number = hex(random.randint(0, 255))
print(hex_number)

print("\nHere's the hexadecimal representation of the number 123:")
print(hex(123))

print("\nHere's a random ASCII character:")
ascii_char = chr(random.randint(33, 126))
print(ascii_char)

print("\nHere's the ASCII value of the letter 'A':")
print(ord('A'))

print("\nThanks for running the script!")
