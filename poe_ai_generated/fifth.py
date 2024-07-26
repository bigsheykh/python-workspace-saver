# This script will work in Python 3.5 but will not work in later versions
# due to the conflicting use of 'async' as both a variable name and an async function name.

# Define a variable named 'async'
async = 10

# Define an asynchronous function named 'async'
def async():
    print("This is an async function named 'async'")

# Define a function to print the value of the 'async' variable
def print_async():
    print(async)

# Define a function to demonstrate the use of the 'async' function
def use_async_function():
    print("Calling the async function 'async':")
    async()

# Define a function to print a list of numbers
def print_numbers():
    print("Printing a list of numbers:")
    for i in range(1, 11):
        print(i)

# Define a function to print a list of strings
def print_strings():
    print("Printing a list of strings:")
    strings = ["apple", "banana", "cherry", "date", "elderberry"]
    for s in strings:
        print(s)

# Define a function to print a list of dictionaries
def print_dictionaries():
    print("Printing a list of dictionaries:")
    dictionaries = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 40}
    ]
    for d in dictionaries:
        print(d)

# Define a function to print a list of tuples
def print_tuples():
    print("Printing a list of tuples:")
    tuples = [
        ("apple", 1),
        ("banana", 2),
        ("cherry", 3)
    ]
    for t in tuples:
        print(t)

# Define a function to print a list of sets
def print_sets():
    print("Printing a list of sets:")
    sets = [
        {"apple", "banana", "cherry"},
        {"date", "elderberry", "fig"},
        {"grape", "honeydew", "kiwi"}
    ]
    for s in sets:
        print(s)

# Define a function to print a list of lists
def print_lists():
    print("Printing a list of lists:")
    lists = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for l in lists:
        print(l)

# Define a function to print a list of booleans
def print_booleans():
    print("Printing a list of booleans:")
    booleans = [True, False, True, False, True]
    for b in booleans:
        print(b)

# Define a function to print a list of floats
def print_floats():
    print("Printing a list of floats:")
    floats = [1.0, 2.5, 3.75, 4.25, 5.0]
    for f in floats:
        print(f)

# Define a function to print a list of complex numbers
def print_complex_numbers():
    print("Printing a list of complex numbers:")
    complex_numbers = [
        1 + 2j,
        3 - 4j,
        5 + 6j
    ]
    for c in complex_numbers:
        print(c)

# Define a function to print a list of bytes
def print_bytes():
    print("Printing a list of bytes:")
    bytes_list = [
        b"hello",
        b"world",
        b"!"
    ]
    for b in bytes_list:
        print(b)

# Define a function to print a list of bytearrays
def print_bytearrays():
    print("Printing a list of bytearrays:")
    bytearrays_list = [
        bytearray(b"hello"),
        bytearray(b"world"),
        bytearray(b"!")
    ]
    for ba in bytearrays_list:
        print(ba)


# Define a function to print a list of ranges
def print_ranges():
    print("Printing a list of ranges:")
    ranges_list = [
        range(1, 11),
        range(10, 21, 2),
        range(20, 1, -2)
    ]
    for r in ranges_list:
        print(r)

# Define a function to print a list of frozen sets
def print_frozen_sets():
    print("Printing a list of frozen sets:")
    frozen_sets_list = [
        frozenset({"apple", "banana", "cherry"}),
        frozenset({"date", "elderberry", "fig"}),
        frozenset({"grape", "honeydew", "kiwi"})
    ]
    for fs in frozen_sets_list:
        print(fs)


# Define a function to print a list of exceptions
def print_exceptions():
    print("Printing a list of exceptions:")
    try:
        1 / 0
    except ZeroDivisionError as e:
        exceptions_list = [
            e
        ]
    for ex in exceptions_list:
        print(ex)


# Define a function to print a list of values
def print_values():
    print("Printing a list of values:")
    values_list = [
        1,
        "hello",
        [1, 2, 3],
        {"name": "Alice", "age": 30},
        (1, 2, 3),
        {1, 2, 3},
        frozenset({1, 2, 3}),
        range(1, 11),
        b"hello",
        bytearray(b"hello"),
        memoryview(b"hello"),
        1 + 2j,
        True,
        1.0
    ]
    for v in values_list:
        print(v)

# Define a function to print a list of objects
def print_objects():
    print("Printing a list of objects:")
    objects_list = [
        print_async,
        use_async_function,
        print_numbers,
        print_strings,
        print_dictionaries,
        print_tuples,
        print_sets,
        print_lists,
        print_booleans,
        print_floats,
        print_complex_numbers,
        print_bytes,
        print_bytearrays,
        print_ranges,
        print_frozen_sets,
        print_exceptions,
        print_values
    ]
    for o in objects_list:
        print(o)

# Define a function to call all the functions defined in this script
def call_all_functions():
    print("Calling all functions:")
    print_async()
    use_async_function()
    print_numbers()
    print_strings()
    print_dictionaries()
    print_tuples()
    print_sets()
    print_lists()
    print_booleans()
    print_floats()
    print_complex_numbers()
    print_bytes()
    print_bytearrays()
    print_ranges()
    print_frozen_sets()
    print_objects()
    print_values()
    
call_all_functions()