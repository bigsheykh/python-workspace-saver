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


import random
import math

save_workspace(7, True, {'random': random})
random_number = random.randint(1, 10)
save_workspace(7, False, {'random_number': random_number, 'random': random})
save_workspace(10, True, {'math': math, 'random_number': random_number})
square_root = math.sqrt(random_number)
save_workspace(10, False, {
    'square_root': square_root,
    'random_number': random_number,
    'math': math
})
save_workspace(13, True, {'print': print, 'random_number': random_number})
print(f'Random number: {random_number}')
save_workspace(13, False, {'print': print, 'random_number': random_number})
save_workspace(14, True, {'print': print, 'square_root': square_root})
print(f'Square root of the random number: {square_root}')
save_workspace(14, False, {'print': print, 'square_root': square_root})
random_numbers = [random.randint(1, 100) for _ in range(10)]
save_workspace(20, True, {'print': print})
print('\nRandom numbers:')
save_workspace(20, False, {'print': print})
for num in random_numbers:
    save_workspace(22, True, {'print': print, 'num': num})
    print(num)
    save_workspace(22, False, {'print': print, 'num': num})
save_workspace(25, True, {'random_numbers': random_numbers, 'sum': sum})
sum_of_numbers = sum(random_numbers)
save_workspace(25, False, {
    'sum_of_numbers': sum_of_numbers,
    'sum': sum,
    'random_numbers': random_numbers
})
save_workspace(28, True, {'print': print, 'sum_of_numbers': sum_of_numbers})
print(f'\nSum of random numbers: {sum_of_numbers}')
save_workspace(28, False, {'print': print, 'sum_of_numbers': sum_of_numbers})
save_workspace(31, True, {
    'sum_of_numbers': sum_of_numbers,
    'len': len,
    'random_numbers': random_numbers
})
average = sum_of_numbers / len(random_numbers)
save_workspace(
    31, False, {
        'average': average,
        'sum_of_numbers': sum_of_numbers,
        'len': len,
        'random_numbers': random_numbers
    })
save_workspace(34, True, {'average': average, 'print': print})
print(f'Average of random numbers: {average}')
save_workspace(34, False, {'average': average, 'print': print})
save_workspace(37, True, {'print': print})
print('\nPython file execution complete. Outputs generated.')
save_workspace(37, False, {'print': print})
