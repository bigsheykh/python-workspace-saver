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


save_workspace(5, True, {})
async = 10
save_workspace(5, False, {'async': async})


def async ():
    save_workspace(9, True, {'print': print})
    print("This is an async function named 'async'")
    save_workspace(9, False, {'print': print})


def print_async():
    save_workspace(13, True, {'print': print, 'async': async})
    print(async)
    save_workspace(13, False, {'print': print, 'async': async})


def use_async_function():
    save_workspace(17, True, {'print': print})
    print("Calling the async function 'async':")
    save_workspace(17, False, {'print': print})
    save_workspace(18, True, {'async': async})
    async ()
    save_workspace(18, False, {'async': async})


def print_numbers():
    save_workspace(22, True, {'print': print})
    print('Printing a list of numbers:')
    save_workspace(22, False, {'print': print})
    for i in range(1, 11):
        save_workspace(24, True, {'print': print, 'i': i})
        print(i)
        save_workspace(24, False, {'print': print, 'i': i})


def print_strings():
    save_workspace(28, True, {'print': print})
    print('Printing a list of strings:')
    save_workspace(28, False, {'print': print})
    save_workspace(29, True, {})
    strings = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    save_workspace(29, False, {'strings': strings})
    for s in strings:
        save_workspace(31, True, {'print': print, 's': s})
        print(s)
        save_workspace(31, False, {'print': print, 's': s})


def print_dictionaries():
    save_workspace(35, True, {'print': print})
    print('Printing a list of dictionaries:')
    save_workspace(35, False, {'print': print})
    save_workspace(36, True, {})
    dictionaries = [{
        'name': 'Alice',
        'age': 30
    }, {
        'name': 'Bob',
        'age': 25
    }, {
        'name': 'Charlie',
        'age': 40
    }]
    save_workspace(36, False, {'dictionaries': dictionaries})
    for d in dictionaries:
        save_workspace(42, True, {'print': print, 'd': d})
        print(d)
        save_workspace(42, False, {'print': print, 'd': d})


def print_tuples():
    save_workspace(46, True, {'print': print})
    print('Printing a list of tuples:')
    save_workspace(46, False, {'print': print})
    save_workspace(47, True, {})
    tuples = [('apple', 1), ('banana', 2), ('cherry', 3)]
    save_workspace(47, False, {'tuples': tuples})
    for t in tuples:
        save_workspace(53, True, {'print': print, 't': t})
        print(t)
        save_workspace(53, False, {'print': print, 't': t})


def print_sets():
    save_workspace(57, True, {'print': print})
    print('Printing a list of sets:')
    save_workspace(57, False, {'print': print})
    save_workspace(58, True, {})
    sets = [{'apple', 'banana', 'cherry'}, {'date', 'elderberry', 'fig'},
            {'grape', 'honeydew', 'kiwi'}]
    save_workspace(58, False, {'sets': sets})
    for s in sets:
        save_workspace(64, True, {'print': print, 's': s})
        print(s)
        save_workspace(64, False, {'print': print, 's': s})


def print_lists():
    save_workspace(68, True, {'print': print})
    print('Printing a list of lists:')
    save_workspace(68, False, {'print': print})
    save_workspace(69, True, {})
    lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    save_workspace(69, False, {'lists': lists})
    for l in lists:
        save_workspace(75, True, {'print': print, 'l': l})
        print(l)
        save_workspace(75, False, {'print': print, 'l': l})


def print_booleans():
    save_workspace(79, True, {'print': print})
    print('Printing a list of booleans:')
    save_workspace(79, False, {'print': print})
    save_workspace(80, True, {})
    booleans = [True, False, True, False, True]
    save_workspace(80, False, {'booleans': booleans})
    for b in booleans:
        save_workspace(82, True, {'print': print, 'b': b})
        print(b)
        save_workspace(82, False, {'print': print, 'b': b})


def print_floats():
    save_workspace(86, True, {'print': print})
    print('Printing a list of floats:')
    save_workspace(86, False, {'print': print})
    save_workspace(87, True, {})
    floats = [1.0, 2.5, 3.75, 4.25, 5.0]
    save_workspace(87, False, {'floats': floats})
    for f in floats:
        save_workspace(89, True, {'print': print, 'f': f})
        print(f)
        save_workspace(89, False, {'print': print, 'f': f})


def print_complex_numbers():
    save_workspace(93, True, {'print': print})
    print('Printing a list of complex numbers:')
    save_workspace(93, False, {'print': print})
    save_workspace(94, True, {})
    complex_numbers = [1 + 2j, 3 - 4j, 5 + 6j]
    save_workspace(94, False, {'complex_numbers': complex_numbers})
    for c in complex_numbers:
        save_workspace(100, True, {'print': print, 'c': c})
        print(c)
        save_workspace(100, False, {'print': print, 'c': c})


def print_bytes():
    save_workspace(104, True, {'print': print})
    print('Printing a list of bytes:')
    save_workspace(104, False, {'print': print})
    save_workspace(105, True, {})
    bytes_list = [b'hello', b'world', b'!']
    save_workspace(105, False, {'bytes_list': bytes_list})
    for b in bytes_list:
        save_workspace(111, True, {'print': print, 'b': b})
        print(b)
        save_workspace(111, False, {'print': print, 'b': b})


def print_bytearrays():
    save_workspace(115, True, {'print': print})
    print('Printing a list of bytearrays:')
    save_workspace(115, False, {'print': print})
    save_workspace(116, True, {'bytearray': bytearray})
    bytearrays_list = [
        bytearray(b'hello'),
        bytearray(b'world'),
        bytearray(b'!')
    ]
    save_workspace(116, False, {
        'bytearrays_list': bytearrays_list,
        'bytearray': bytearray
    })
    for ba in bytearrays_list:
        save_workspace(122, True, {'print': print, 'ba': ba})
        print(ba)
        save_workspace(122, False, {'print': print, 'ba': ba})


def print_ranges():
    save_workspace(127, True, {'print': print})
    print('Printing a list of ranges:')
    save_workspace(127, False, {'print': print})
    save_workspace(128, True, {'range': range})
    ranges_list = [range(1, 11), range(10, 21, 2), range(20, 1, -2)]
    save_workspace(128, False, {'range': range, 'ranges_list': ranges_list})
    for r in ranges_list:
        save_workspace(134, True, {'print': print, 'r': r})
        print(r)
        save_workspace(134, False, {'print': print, 'r': r})


def print_frozen_sets():
    save_workspace(138, True, {'print': print})
    print('Printing a list of frozen sets:')
    save_workspace(138, False, {'print': print})
    save_workspace(139, True, {'frozenset': frozenset})
    frozen_sets_list = [
        frozenset({'apple', 'banana', 'cherry'}),
        frozenset({'date', 'elderberry', 'fig'}),
        frozenset({'grape', 'honeydew', 'kiwi'})
    ]
    save_workspace(139, False, {
        'frozen_sets_list': frozen_sets_list,
        'frozenset': frozenset
    })
    for fs in frozen_sets_list:
        save_workspace(145, True, {'print': print, 'fs': fs})
        print(fs)
        save_workspace(145, False, {'print': print, 'fs': fs})


def print_exceptions():
    save_workspace(150, True, {'print': print})
    print('Printing a list of exceptions:')
    save_workspace(150, False, {'print': print})
    try:
        1 / 0
    except ZeroDivisionError as e:
        exceptions_list = [e]
    for ex in exceptions_list:
        save_workspace(158, True, {'print': print, 'ex': ex})
        print(ex)
        save_workspace(158, False, {'print': print, 'ex': ex})


def print_values():
    save_workspace(163, True, {'print': print})
    print('Printing a list of values:')
    save_workspace(163, False, {'print': print})
    save_workspace(
        164, True, {
            'range': range,
            'memoryview': memoryview,
            'bytearray': bytearray,
            'frozenset': frozenset
        })
    values_list = [
        1, 'hello', [1, 2, 3], {
            'name': 'Alice',
            'age': 30
        }, (1, 2, 3), {1, 2, 3},
        frozenset({1, 2, 3}),
        range(1, 11), b'hello',
        bytearray(b'hello'),
        memoryview(b'hello'), 1 + 2j, True, 1.0
    ]
    save_workspace(
        164, False, {
            'range': range,
            'frozenset': frozenset,
            'values_list': values_list,
            'bytearray': bytearray,
            'memoryview': memoryview
        })
    for v in values_list:
        save_workspace(181, True, {'print': print, 'v': v})
        print(v)
        save_workspace(181, False, {'print': print, 'v': v})


def print_objects():
    save_workspace(185, True, {'print': print})
    print('Printing a list of objects:')
    save_workspace(185, False, {'print': print})
    save_workspace(
        186, True, {
            'print_tuples': print_tuples,
            'print_strings': print_strings,
            'print_frozen_sets': print_frozen_sets,
            'print_async': print_async,
            'print_floats': print_floats,
            'print_booleans': print_booleans,
            'print_bytearrays': print_bytearrays,
            'print_values': print_values,
            'print_complex_numbers': print_complex_numbers,
            'print_numbers': print_numbers,
            'print_lists': print_lists,
            'use_async_function': use_async_function,
            'print_dictionaries': print_dictionaries,
            'print_sets': print_sets,
            'print_ranges': print_ranges,
            'print_exceptions': print_exceptions,
            'print_bytes': print_bytes
        })
    objects_list = [
        print_async, use_async_function, print_numbers, print_strings,
        print_dictionaries, print_tuples, print_sets, print_lists,
        print_booleans, print_floats, print_complex_numbers, print_bytes,
        print_bytearrays, print_ranges, print_frozen_sets, print_exceptions,
        print_values
    ]
    save_workspace(
        186, False, {
            'objects_list': objects_list,
            'print_tuples': print_tuples,
            'print_strings': print_strings,
            'print_frozen_sets': print_frozen_sets,
            'print_async': print_async,
            'print_floats': print_floats,
            'print_booleans': print_booleans,
            'print_bytearrays': print_bytearrays,
            'print_values': print_values,
            'print_complex_numbers': print_complex_numbers,
            'print_numbers': print_numbers,
            'print_lists': print_lists,
            'use_async_function': use_async_function,
            'print_dictionaries': print_dictionaries,
            'print_sets': print_sets,
            'print_ranges': print_ranges,
            'print_exceptions': print_exceptions,
            'print_bytes': print_bytes
        })
    for o in objects_list:
        save_workspace(206, True, {'print': print, 'o': o})
        print(o)
        save_workspace(206, False, {'print': print, 'o': o})


def call_all_functions():
    save_workspace(210, True, {'print': print})
    print('Calling all functions:')
    save_workspace(210, False, {'print': print})
    save_workspace(211, True, {'print_async': print_async})
    print_async()
    save_workspace(211, False, {'print_async': print_async})
    save_workspace(212, True, {'use_async_function': use_async_function})
    use_async_function()
    save_workspace(212, False, {'use_async_function': use_async_function})
    save_workspace(213, True, {'print_numbers': print_numbers})
    print_numbers()
    save_workspace(213, False, {'print_numbers': print_numbers})
    save_workspace(214, True, {'print_strings': print_strings})
    print_strings()
    save_workspace(214, False, {'print_strings': print_strings})
    save_workspace(215, True, {'print_dictionaries': print_dictionaries})
    print_dictionaries()
    save_workspace(215, False, {'print_dictionaries': print_dictionaries})
    save_workspace(216, True, {'print_tuples': print_tuples})
    print_tuples()
    save_workspace(216, False, {'print_tuples': print_tuples})
    save_workspace(217, True, {'print_sets': print_sets})
    print_sets()
    save_workspace(217, False, {'print_sets': print_sets})
    save_workspace(218, True, {'print_lists': print_lists})
    print_lists()
    save_workspace(218, False, {'print_lists': print_lists})
    save_workspace(219, True, {'print_booleans': print_booleans})
    print_booleans()
    save_workspace(219, False, {'print_booleans': print_booleans})
    save_workspace(220, True, {'print_floats': print_floats})
    print_floats()
    save_workspace(220, False, {'print_floats': print_floats})
    save_workspace(221, True, {'print_complex_numbers': print_complex_numbers})
    print_complex_numbers()
    save_workspace(221, False,
                   {'print_complex_numbers': print_complex_numbers})
    save_workspace(222, True, {'print_bytes': print_bytes})
    print_bytes()
    save_workspace(222, False, {'print_bytes': print_bytes})
    save_workspace(223, True, {'print_bytearrays': print_bytearrays})
    print_bytearrays()
    save_workspace(223, False, {'print_bytearrays': print_bytearrays})
    save_workspace(224, True, {'print_ranges': print_ranges})
    print_ranges()
    save_workspace(224, False, {'print_ranges': print_ranges})
    save_workspace(225, True, {'print_frozen_sets': print_frozen_sets})
    print_frozen_sets()
    save_workspace(225, False, {'print_frozen_sets': print_frozen_sets})
    save_workspace(226, True, {'print_objects': print_objects})
    print_objects()
    save_workspace(226, False, {'print_objects': print_objects})
    save_workspace(227, True, {'print_values': print_values})
    print_values()
    save_workspace(227, False, {'print_values': print_values})


save_workspace(229, True, {'call_all_functions': call_all_functions})
call_all_functions()
save_workspace(229, False, {'call_all_functions': call_all_functions})
