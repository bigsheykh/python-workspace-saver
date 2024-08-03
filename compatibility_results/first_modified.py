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


import binascii

save_workspace(9, True, {})
simple_string = 'SGVsbG8sIFB5dGh'
save_workspace(9, False, {'simple_string': simple_string})
save_workspace(12, True, {
    'binascii': binascii,
    'simple_string': simple_string
})
coded_bytes = binascii.b2a_hqx(simple_string.encode())
save_workspace(
    12, False, {
        'binascii': binascii,
        'coded_bytes': coded_bytes,
        'simple_string': simple_string
    })
save_workspace(13, True, {'coded_bytes': coded_bytes, 'print': print})
print(coded_bytes)
save_workspace(13, False, {'coded_bytes': coded_bytes, 'print': print})
save_workspace(16, True, {'binascii': binascii, 'coded_bytes': coded_bytes})
decoded_bytes = binascii.a2b_hqx(coded_bytes)
save_workspace(
    16, False, {
        'binascii': binascii,
        'coded_bytes': coded_bytes,
        'decoded_bytes': decoded_bytes
    })
save_workspace(17, True, {'decoded_bytes': decoded_bytes, 'print': print})
print(decoded_bytes)
save_workspace(17, False, {'decoded_bytes': decoded_bytes, 'print': print})
save_workspace(20, True, {'decoded_bytes': decoded_bytes})
decoded_string = decoded_bytes[0].decode()
save_workspace(20, False, {
    'decoded_string': decoded_string,
    'decoded_bytes': decoded_bytes
})
save_workspace(23, True, {'decoded_string': decoded_string, 'print': print})
print('Decoded String:', decoded_string)
save_workspace(23, False, {'decoded_string': decoded_string, 'print': print})
save_workspace(26, True, {})
a = 10
save_workspace(26, False, {'a': a})
save_workspace(27, True, {})
b = 20
save_workspace(27, False, {'b': b})
save_workspace(28, True, {'a': a, 'b': b})
c = a + b
save_workspace(28, False, {'a': a, 'c': c, 'b': b})
save_workspace(31, True, {'c': c, 'print': print})
print('Result of the calculation:', c)
save_workspace(31, False, {'c': c, 'print': print})
save_workspace(34, True, {})
numbers = [1, 2, 3, 4, 5]
save_workspace(34, False, {'numbers': numbers})
save_workspace(37, True, {'sum': sum, 'numbers': numbers})
sum_of_numbers = sum(numbers)
save_workspace(37, False, {
    'sum_of_numbers': sum_of_numbers,
    'numbers': numbers,
    'sum': sum
})
save_workspace(40, True, {'sum_of_numbers': sum_of_numbers, 'print': print})
print('Sum of the numbers:', sum_of_numbers)
save_workspace(40, False, {'sum_of_numbers': sum_of_numbers, 'print': print})
save_workspace(43, True, {})
fibonacci = [0, 1]
save_workspace(43, False, {'fibonacci': fibonacci})
save_workspace(44, True, {})
limit = 10
save_workspace(44, False, {'limit': limit})
while len(fibonacci) < limit:
    save_workspace(47, True, {'fibonacci': fibonacci})
    next_number = fibonacci[-1] + fibonacci[-2]
    save_workspace(47, False, {
        'next_number': next_number,
        'fibonacci': fibonacci
    })
    save_workspace(48, True, {
        'next_number': next_number,
        'fibonacci': fibonacci
    })
    fibonacci.append(next_number)
    save_workspace(48, False, {
        'next_number': next_number,
        'fibonacci': fibonacci
    })
save_workspace(51, True, {'fibonacci': fibonacci, 'print': print})
print('Fibonacci sequence:', fibonacci)
save_workspace(51, False, {'fibonacci': fibonacci, 'print': print})
save_workspace(54, True, {})
person = {'name': 'John', 'age': 30, 'city': 'New York'}
save_workspace(54, False, {'person': person})
save_workspace(61, True, {'person': person, 'print': print})
print('Person details:', person)
save_workspace(61, False, {'person': person, 'print': print})
save_workspace(64, True, {})
text = 'Hello, World!'
save_workspace(64, False, {'text': text})
if text.startswith('Hello'):
    save_workspace(68, True, {'print': print})
    print("The string starts with 'Hello'")
    save_workspace(68, False, {'print': print})
else:
    save_workspace(70, True, {'print': print})
    print("The string does not start with 'Hello'")
    save_workspace(70, False, {'print': print})
save_workspace(73, True, {'text': text})
count = text.count('o')
save_workspace(73, False, {'text': text, 'count': count})
save_workspace(76, True, {'count': count, 'print': print})
print("Count of 'o':", count)
save_workspace(76, False, {'count': count, 'print': print})
save_workspace(79, True, {'a': a, 'c': c, 'b': b})
formatted_string = f'The sum of {a} and {b} is {c}'
save_workspace(79, False, {
    'a': a,
    'c': c,
    'formatted_string': formatted_string,
    'b': b
})
save_workspace(82, True, {
    'formatted_string': formatted_string,
    'print': print
})
print('Formatted string:', formatted_string)
save_workspace(82, False, {
    'formatted_string': formatted_string,
    'print': print
})
save_workspace(85, True, {})
T = 'Hiya'
save_workspace(85, False, {'T': T})
save_workspace(86, True, {})
val = [1, 2, 3]
save_workspace(86, False, {'val': val})
