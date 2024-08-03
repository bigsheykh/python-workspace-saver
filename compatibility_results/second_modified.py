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
import random
import datetime

save_workspace(5, True, {'print': print})
print('Welcome to the Python script with no inputs!')
save_workspace(5, False, {'print': print})
save_workspace(7, True, {'print': print})
print('Here are some random numbers:')
save_workspace(7, False, {'print': print})
for i in range(10):
    save_workspace(9, True, {'print': print, 'random': random})
    print(random.randint(1, 100))
    save_workspace(9, False, {'print': print, 'random': random})
save_workspace(11, True, {'print': print})
print('\nHere are some mathematical calculations:')
save_workspace(11, False, {'print': print})
save_workspace(12, True, {'print': print, 'math': math})
print('The value of pi is:', math.pi)
save_workspace(12, False, {'print': print, 'math': math})
save_workspace(13, True, {'print': print, 'math': math})
print('The square root of 25 is:', math.sqrt(25))
save_workspace(13, False, {'print': print, 'math': math})
save_workspace(14, True, {'print': print, 'math': math})
print('The sine of 45 degrees is:', math.sin(math.radians(45)))
save_workspace(14, False, {'print': print, 'math': math})
save_workspace(16, True, {'print': print})
print("\nHere's the current date and time:")
save_workspace(16, False, {'print': print})
save_workspace(17, True, {'datetime': datetime})
now = datetime.datetime.now()
save_workspace(17, False, {'now': now, 'datetime': datetime})
save_workspace(18, True, {'now': now, 'print': print})
print(now.strftime('%Y-%m-%d %H:%M:%S'))
save_workspace(18, False, {'now': now, 'print': print})
save_workspace(20, True, {'print': print})
print("\nHere's a random joke:")
save_workspace(20, False, {'print': print})
save_workspace(21, True, {})
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    'Why was the math book sad? Because of all of its problems!',
    "Why can't a bicycle stand up by itself? Because it's two-tired!",
    'Why did the tomato turn red? Because it saw the salad dressing!',
    'Why did the scarecrow win an award? Because he was outstanding in his field!'
]
save_workspace(21, False, {'jokes': jokes})
save_workspace(28, True, {'jokes': jokes, 'print': print, 'random': random})
print(random.choice(jokes))
save_workspace(28, False, {'jokes': jokes, 'print': print, 'random': random})
save_workspace(30, True, {'print': print})
print("\nHere's a list of the first 20 Fibonacci numbers:")
save_workspace(30, False, {'print': print})
save_workspace(31, True, {})
a, b = (0, 1)
save_workspace(31, False, {'a': a, 'b': b})
save_workspace(32, True, {'a': a, 'b': b})
fibonacci_numbers = [a, b]
save_workspace(32, False, {
    'a': a,
    'fibonacci_numbers': fibonacci_numbers,
    'b': b
})
for i in range(18):
    save_workspace(34, True, {'a': a, 'b': b})
    a, b = (b, a + b)
    save_workspace(34, False, {'a': a, 'b': b})
    save_workspace(35, True, {'fibonacci_numbers': fibonacci_numbers, 'b': b})
    fibonacci_numbers.append(b)
    save_workspace(35, False, {'fibonacci_numbers': fibonacci_numbers, 'b': b})
save_workspace(36, True, {
    'print': print,
    'fibonacci_numbers': fibonacci_numbers
})
print(fibonacci_numbers)
save_workspace(36, False, {
    'print': print,
    'fibonacci_numbers': fibonacci_numbers
})
save_workspace(38, True, {'print': print})
print("\nHere's a random binary number:")
save_workspace(38, False, {'print': print})
save_workspace(39, True, {'random': random})
binary_number = ''.join(random.choices(['0', '1'], k=8))
save_workspace(39, False, {'binary_number': binary_number, 'random': random})
save_workspace(40, True, {'print': print, 'binary_number': binary_number})
print(binary_number)
save_workspace(40, False, {'print': print, 'binary_number': binary_number})
save_workspace(42, True, {'print': print})
print("\nHere's the binary representation of the number 42:")
save_workspace(42, False, {'print': print})
save_workspace(43, True, {'print': print, 'bin': bin})
print(bin(42))
save_workspace(43, False, {'print': print, 'bin': bin})
save_workspace(45, True, {'print': print})
print("\nHere's a random hexadecimal number:")
save_workspace(45, False, {'print': print})
save_workspace(46, True, {'random': random, 'hex': hex})
hex_number = hex(random.randint(0, 255))
save_workspace(46, False, {
    'hex': hex,
    'hex_number': hex_number,
    'random': random
})
save_workspace(47, True, {'print': print, 'hex_number': hex_number})
print(hex_number)
save_workspace(47, False, {'print': print, 'hex_number': hex_number})
save_workspace(49, True, {'print': print})
print("\nHere's the hexadecimal representation of the number 123:")
save_workspace(49, False, {'print': print})
save_workspace(50, True, {'print': print, 'hex': hex})
print(hex(123))
save_workspace(50, False, {'print': print, 'hex': hex})
save_workspace(52, True, {'print': print})
print("\nHere's a random ASCII character:")
save_workspace(52, False, {'print': print})
save_workspace(53, True, {'chr': chr, 'random': random})
ascii_char = chr(random.randint(33, 126))
save_workspace(53, False, {
    'chr': chr,
    'ascii_char': ascii_char,
    'random': random
})
save_workspace(54, True, {'print': print, 'ascii_char': ascii_char})
print(ascii_char)
save_workspace(54, False, {'print': print, 'ascii_char': ascii_char})
save_workspace(56, True, {'print': print})
print("\nHere's the ASCII value of the letter 'A':")
save_workspace(56, False, {'print': print})
save_workspace(57, True, {'print': print, 'ord': ord})
print(ord('A'))
save_workspace(57, False, {'print': print, 'ord': ord})
save_workspace(59, True, {'print': print})
print('\nThanks for running the script!')
save_workspace(59, False, {'print': print})
