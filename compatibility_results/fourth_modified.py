import shelve
import os
import base64


def save_workspace(line_number, is_before_line, dict_of_values_to_save):
    os.makedirs('/tmp/python-workspace/', exist_ok=True)
    dir_name = base64.b64encode(os.path.abspath(__file__).encode()).decode()
    py_directory = '/tmp/python-workspace/' + dir_name
    os.makedirs(py_directory, exist_ok=True)
    line_directory = py_directory + '/' + str(line_number)
    os.makedirs(line_directory, exist_ok=True)
    file_name = line_directory + '/' + str(is_before_line)
    my_shelf = shelve.open(file_name, 'n')
    for key in globals().keys():
        try:
            my_shelf[key] = globals()[key]
        except TypeError:
            print('TypeError shelving:', key)
        except:
            print('Error shelving:', key)
    for key in dict_of_values_to_save.keys():
        try:
            my_shelf[key] = dict_of_values_to_save[key]
        except TypeError:
            print('TypeError shelving:', key)
        except:
            print('TypeError shelving:', key)
    my_shelf.close()


import math
import datetime
import string
import itertools


def fibonacci(n):
    save_workspace(8, True, {})
    a, b = (0, 1)
    save_workspace(8, False, {'b': b, 'a': a})
    save_workspace(9, True, {})
    sequence = []
    save_workspace(9, False, {'sequence': sequence})
    for _ in range(n):
        save_workspace(11, True, {'sequence': sequence, 'a': a})
        sequence.append(a)
        save_workspace(11, False, {'sequence': sequence, 'a': a})
        save_workspace(12, True, {'b': b, 'a': a})
        a, b = (b, a + b)
        save_workspace(12, False, {'b': b, 'a': a})
    return sequence


def fibonacci_sum(n):
    return sum(fibonacci(n))


def factorials(n):
    return [math.factorial(i) for i in range(n + 1)]


def palindromic_numbers(limit):
    return [num for num in range(1, limit + 1) if str(num) == str(num)[::-1]]


def pythagorean_triples(limit):
    return [(a, b, c) for a in range(1, limit + 1)
            for b in range(a, limit + 1) for c in range(b, limit + 1)
            if a**2 + b**2 == c**2]


def leap_years(start, end):
    return [
        year for year in range(start, end + 1)
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    ]


def prime_numbers(limit):
    save_workspace(41, True, {})
    primes = []
    save_workspace(41, False, {'primes': primes})
    for num in range(2, limit + 1):
        is_prime = all((num % i != 0 for i in range(2,
                                                    int(math.sqrt(num)) + 1)))
        if is_prime:
            save_workspace(45, True, {'primes': primes, 'num': num})
            primes.append(num)
            save_workspace(45, False, {'primes': primes, 'num': num})
    return primes


save_workspace(49, True, {'fibonacci': fibonacci})
fib_sequence = fibonacci(20)
save_workspace(49, False, {
    'fibonacci': fibonacci,
    'fib_sequence': fib_sequence
})
save_workspace(50, True, {'fibonacci_sum': fibonacci_sum})
fib_sum = fibonacci_sum(20)
save_workspace(50, False, {'fib_sum': fib_sum, 'fibonacci_sum': fibonacci_sum})
save_workspace(51, True, {'math': math})
fact_of_10 = math.factorial(10)
save_workspace(51, False, {'math': math, 'fact_of_10': fact_of_10})
save_workspace(52, True, {'palindromic_numbers': palindromic_numbers})
palindromes = palindromic_numbers(1000)
save_workspace(52, False, {
    'palindromes': palindromes,
    'palindromic_numbers': palindromic_numbers
})
save_workspace(53, True, {'pythagorean_triples': pythagorean_triples})
pythagorean = pythagorean_triples(20)
save_workspace(53, False, {
    'pythagorean_triples': pythagorean_triples,
    'pythagorean': pythagorean
})
save_workspace(54, True, {'leap_years': leap_years})
leaps = leap_years(2000, 2100)
save_workspace(54, False, {'leaps': leaps, 'leap_years': leap_years})
save_workspace(55, True, {'prime_numbers': prime_numbers})
primes = prime_numbers(100)
save_workspace(55, False, {'primes': primes, 'prime_numbers': prime_numbers})
save_workspace(56, True, {'datetime': datetime})
current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
save_workspace(56, False, {'current_time': current_time, 'datetime': datetime})
save_workspace(57, True, {'math': math})
pi_value = math.pi
save_workspace(57, False, {'math': math, 'pi_value': pi_value})
save_workspace(60, True, {'print': print, 'fib_sequence': fib_sequence})
print('Fibonacci sequence:', fib_sequence)
save_workspace(60, False, {'print': print, 'fib_sequence': fib_sequence})
save_workspace(61, True, {'fib_sum': fib_sum, 'print': print})
print('Sum of Fibonacci sequence:', fib_sum)
save_workspace(61, False, {'fib_sum': fib_sum, 'print': print})
save_workspace(62, True, {'fact_of_10': fact_of_10, 'print': print})
print('Factorial of 10:', fact_of_10)
save_workspace(62, False, {'fact_of_10': fact_of_10, 'print': print})
save_workspace(63, True, {'palindromes': palindromes, 'print': print})
print('Palindromic numbers up to 1000:', palindromes)
save_workspace(63, False, {'palindromes': palindromes, 'print': print})
save_workspace(64, True, {'print': print, 'pythagorean': pythagorean})
print('Pythagorean triples up to 20:', pythagorean)
save_workspace(64, False, {'print': print, 'pythagorean': pythagorean})
save_workspace(65, True, {'leaps': leaps, 'print': print})
print('Leap years from 2000 to 2100:', leaps)
save_workspace(65, False, {'leaps': leaps, 'print': print})
save_workspace(66, True, {'primes': primes, 'print': print})
print('Prime numbers up to 100:', primes)
save_workspace(66, False, {'primes': primes, 'print': print})
save_workspace(67, True, {'current_time': current_time, 'print': print})
print('Current date and time:', current_time)
save_workspace(67, False, {'current_time': current_time, 'print': print})
save_workspace(68, True, {'print': print, 'pi_value': pi_value})
print('Value of pi:', pi_value)
save_workspace(68, False, {'print': print, 'pi_value': pi_value})
ascii_chars = [chr(i) for i in range(32, 127)]
binary_numbers = [bin(i)[2:].zfill(8) for i in range(256)]
hex_numbers = [hex(i)[2:].zfill(2) for i in range(256)]
save_workspace(77, True, {'string': string})
letters = string.ascii_letters
save_workspace(77, False, {'string': string, 'letters': letters})
permutations = [''.join(p) for p in itertools.permutations(letters[:4])]
combinations = [
    ''.join(map(str, c)) for c in itertools.combinations(range(10), 5)
]
save_workspace(
    82, True, {
        'hex_numbers': hex_numbers,
        'ascii_chars': ascii_chars,
        'combinations': combinations,
        'binary_numbers': binary_numbers,
        'permutations': permutations
    })
results = {
    'ASCII characters': ascii_chars,
    'Binary numbers': binary_numbers,
    'Hex numbers': hex_numbers,
    'Permutations of 4 letters': permutations,
    'Combinations of 5 numbers': combinations
}
save_workspace(
    82, False, {
        'results': results,
        'hex_numbers': hex_numbers,
        'combinations': combinations,
        'binary_numbers': binary_numbers,
        'ascii_chars': ascii_chars,
        'permutations': permutations
    })
save_workspace(98, True, {'print': print})
print('Output generation complete.')
save_workspace(98, False, {'print': print})
