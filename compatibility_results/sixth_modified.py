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


from typing import List, Tuple, Dict, Set, Union, Optional
from dataclasses import dataclass
from enum import Enum, auto
from collections import namedtuple
from functools import lru_cache
from time import sleep
import math
import asyncio


@dataclass
class Person:
    """
    A simple dataclass representing a person.
    """
    name: str
    age: int
    occupation: str = 'Unknown'


class TrafficLight(Enum):
    """
    An enum representing traffic light colors.
    """
    RED = auto()
    YELLOW = auto()
    GREEN = auto()


save_workspace(29, True, {'namedtuple': namedtuple})
Point = namedtuple('Point', ['x', 'y'])
save_workspace(29, False, {'namedtuple': namedtuple, 'Point': Point})


def sum_and_average(numbers: List[int]) -> Tuple[int, float]:
    """
    Calculates the sum and average of a list of integers.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and average of the numbers.
    """
    save_workspace(42, True, {'sum': sum, 'numbers': numbers})
    total = sum(numbers)
    save_workspace(42, False, {'sum': sum, 'total': total, 'numbers': numbers})
    save_workspace(43, True, {'len': len, 'total': total, 'numbers': numbers})
    average = total / len(numbers)
    save_workspace(43, False, {
        'total': total,
        'numbers': numbers,
        'average': average,
        'len': len
    })
    return (total, average)


def demonstrate_typing():
    """
    Demonstrates the use of type hints in Python 3.
    """
    save_workspace(52, True, {})
    numbers = [1, 2, 3, 4, 5]
    save_workspace(52, False, {'numbers': numbers})
    save_workspace(53, True, {
        'sum_and_average': sum_and_average,
        'numbers': numbers
    })
    sum, average = sum_and_average(numbers)
    save_workspace(
        53, False, {
            'sum_and_average': sum_and_average,
            'sum': sum,
            'average': average,
            'numbers': numbers
        })
    save_workspace(56, True, {'sum': sum, 'print': print})
    print(f'Sum: {sum}')
    save_workspace(56, False, {'sum': sum, 'print': print})
    save_workspace(57, True, {'print': print, 'average': average})
    print(f'Average: {average}')
    save_workspace(57, False, {'print': print, 'average': average})


@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    """
    Calculates the nth Fibonacci number using memoization.

    Args:
        n: The index of the Fibonacci number to calculate.

    Returns:
        The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def demonstrate_lru_cache():
    """
    Demonstrates the use of LRU cache in Python 3.2.
    """
    for i in range(10):
        save_workspace(83, True, {
            'i': i,
            'fibonacci': fibonacci,
            'print': print
        })
        print(f'Fibonacci({i}): {fibonacci(i)}')
        save_workspace(83, False, {
            'i': i,
            'fibonacci': fibonacci,
            'print': print
        })


async def count_to_ten():
    """
    Asynchronously counts from 1 to 10 with delays.
    """
    for i in range(1, 11):
        save_workspace(90, True, {'i': i, 'print': print})
        print(f'Counting: {i}')
        save_workspace(90, False, {'i': i, 'print': print})
        save_workspace(91, True, {'sleep': sleep})
        sleep(1)
        save_workspace(91, False, {'sleep': sleep})


async def main():
    """
    Main function to run the asynchronous task.
    """
    await count_to_ten()


def demonstrate_async_await():
    """
    Demonstrates the use of async/await in Python 3.5.
    """
    save_workspace(106, True, {'main': main, 'asyncio': asyncio})
    asyncio.run(main())
    save_workspace(106, False, {'main': main, 'asyncio': asyncio})


def demonstrate_match_case():
    """
    Demonstrates the use of match-case in Python 3.10.
    """
    save_workspace(114, True, {})
    value = 10
    save_workspace(114, False, {'value': value})
    match value:
        case 10:
            save_workspace(119, True, {'print': print})
            print('Value is 10')
            save_workspace(119, False, {'print': print})
        case 20:
            save_workspace(121, True, {'print': print})
            print('Value is 20')
            save_workspace(121, False, {'print': print})
        case _:
            save_workspace(123, True, {'print': print})
            print('Value is not 10 or 20')
            save_workspace(123, False, {'print': print})


def greet(name: str | int) -> str:
    """
    Greets the user with a personalized message.

    Args:
        name: The name of the user.

    Returns:
        A greeting message.
    """
    if isinstance(name, str):
        return f'Hello, {name}!'
    else:
        return f'Hello, user {name}!'


def demonstrate_union_operator():
    """
    Demonstrates the use of the union operator (|) in Python 3.10.
    """
    save_workspace(148, True, {'greet': greet, 'print': print})
    print(greet('Alice'))
    save_workspace(148, False, {'greet': greet, 'print': print})
    save_workspace(149, True, {'greet': greet, 'print': print})
    print(greet(123))
    save_workspace(149, False, {'greet': greet, 'print': print})


def demonstrate_strict_float_parsing():
    """
    Demonstrates the use of strict float parsing in Python 3.11.
    """
    try:
        save_workspace(158, True, {'float': float})
        float('1.0e+5')
        save_workspace(158, False, {'float': float})
        save_workspace(159, True, {'print': print})
        print('Strict float parsing successful')
        save_workspace(159, False, {'print': print})
    except ValueError:
        print('Strict float parsing failed')


def demonstrate_new_math_functions():
    """
    Demonstrates the use of new math functions in Python 3.11.
    """
    save_workspace(169, True, {'math': math, 'print': print})
    print(f'math.cbrt(8): {math.cbrt(8)}')
    save_workspace(169, False, {'math': math, 'print': print})
    save_workspace(170, True, {'math': math, 'print': print})
    print(f'math.dist([0, 0], [3, 4]): {math.dist([0, 0], [3, 4])}')
    save_workspace(170, False, {'math': math, 'print': print})


if __name__ == '__main__':
    save_workspace(173, True, {'demonstrate_typing': demonstrate_typing})
    demonstrate_typing()
    save_workspace(173, False, {'demonstrate_typing': demonstrate_typing})
    save_workspace(174, True, {'demonstrate_lru_cache': demonstrate_lru_cache})
    demonstrate_lru_cache()
    save_workspace(174, False,
                   {'demonstrate_lru_cache': demonstrate_lru_cache})
    save_workspace(175, True,
                   {'demonstrate_async_await': demonstrate_async_await})
    demonstrate_async_await()
    save_workspace(175, False,
                   {'demonstrate_async_await': demonstrate_async_await})
    save_workspace(176, True,
                   {'demonstrate_match_case': demonstrate_match_case})
    demonstrate_match_case()
    save_workspace(176, False,
                   {'demonstrate_match_case': demonstrate_match_case})
    save_workspace(177, True,
                   {'demonstrate_union_operator': demonstrate_union_operator})
    demonstrate_union_operator()
    save_workspace(177, False,
                   {'demonstrate_union_operator': demonstrate_union_operator})
    save_workspace(
        178, True,
        {'demonstrate_strict_float_parsing': demonstrate_strict_float_parsing})
    demonstrate_strict_float_parsing()
    save_workspace(
        178, False,
        {'demonstrate_strict_float_parsing': demonstrate_strict_float_parsing})
    save_workspace(
        179, True,
        {'demonstrate_new_math_functions': demonstrate_new_math_functions})
    demonstrate_new_math_functions()
    save_workspace(
        179, False,
        {'demonstrate_new_math_functions': demonstrate_new_math_functions})
