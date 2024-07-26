import math
import datetime
import string
import itertools

# Function to generate Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Function to calculate the sum of Fibonacci sequence
def fibonacci_sum(n):
    return sum(fibonacci(n))

# Function to calculate factorials
def factorials(n):
    return [math.factorial(i) for i in range(n + 1)]

# Function to find palindromic numbers
def palindromic_numbers(limit):
    return [num for num in range(1, limit + 1) if str(num) == str(num)[::-1]]

# Function to find Pythagorean triples
def pythagorean_triples(limit):
    return [(a, b, c) for a in range(1, limit + 1)
            for b in range(a, limit + 1)
            for c in range(b, limit + 1)
            if a ** 2 + b ** 2 == c ** 2]

# Function to find leap years
def leap_years(start, end):
    return [year for year in range(start, end + 1)
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0]

# Function to find prime numbers
def prime_numbers(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))
        if is_prime:
            primes.append(num)
    return primes

# Generate outputs
fib_sequence = fibonacci(20)
fib_sum = fibonacci_sum(20)
fact_of_10 = math.factorial(10)
palindromes = palindromic_numbers(1000)
pythagorean = pythagorean_triples(20)
leaps = leap_years(2000, 2100)
primes = prime_numbers(100)
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
pi_value = math.pi

# Print results
print("Fibonacci sequence:", fib_sequence)
print("Sum of Fibonacci sequence:", fib_sum)
print("Factorial of 10:", fact_of_10)
print("Palindromic numbers up to 1000:", palindromes)
print("Pythagorean triples up to 20:", pythagorean)
print("Leap years from 2000 to 2100:", leaps)
print("Prime numbers up to 100:", primes)
print("Current date and time:", current_time)
print("Value of pi:", pi_value)

# Additional calculations to exceed 100 lines
# Generate character sets
ascii_chars = [chr(i) for i in range(32, 127)]
binary_numbers = [bin(i)[2:].zfill(8) for i in range(256)]
hex_numbers = [hex(i)[2:].zfill(2) for i in range(256)]

# Generate permutations and combinations
letters = string.ascii_letters
permutations = [''.join(p) for p in itertools.permutations(letters[:4])]
combinations = [''.join(map(str, c)) for c in itertools.combinations(range(10), 5)]

# Store results in lists for further processing if needed
results = {
    "ASCII characters": ascii_chars,
    "Binary numbers": binary_numbers,
    "Hex numbers": hex_numbers,
    "Permutations of 4 letters": permutations,
    "Combinations of 5 numbers": combinations
}

# Optionally print additional results
# Uncomment to see the additional results
# print("ASCII characters:", ascii_chars)
# print("Binary numbers:", binary_numbers)
# print("Hex numbers:", hex_numbers)
# print("Permutations of 4 letters:", permutations)
# print("Combinations of 5 numbers:", combinations)

print("Output generation complete.")