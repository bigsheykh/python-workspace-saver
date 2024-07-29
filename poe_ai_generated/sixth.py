# python_3_11_features.py

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
    occupation: str = "Unknown"

class TrafficLight(Enum):
    """
    An enum representing traffic light colors.
    """
    RED = auto()
    YELLOW = auto()
    GREEN = auto()

Point = namedtuple("Point", ["x", "y"])

# Define a function that takes a list of integers and returns a tuple of integers
def sum_and_average(numbers: List[int]) -> Tuple[int, float]:
    """
    Calculates the sum and average of a list of integers.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and average of the numbers.
    """
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

def demonstrate_typing():
    """
    Demonstrates the use of type hints in Python 3.
    """

    # Call the function with a list of integers
    numbers = [1, 2, 3, 4, 5]
    sum, average = sum_and_average(numbers)

    # Print the sum and average
    print(f"Sum: {sum}")
    print(f"Average: {average}")

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
        return fibonacci(n-1) + fibonacci(n-2)

def demonstrate_lru_cache():
    """
    Demonstrates the use of LRU cache in Python 3.2.
    """


    # Calculate and print the first 10 Fibonacci numbers
    for i in range(10):
        print(f"Fibonacci({i}): {fibonacci(i)}")

async def count_to_ten():
    """
    Asynchronously counts from 1 to 10 with delays.
    """
    for i in range(1, 11):
        print(f"Counting: {i}")
        sleep(1)

async def main():
    """
    Main function to run the asynchronous task.
    """
    await count_to_ten()

def demonstrate_async_await():
    """
    Demonstrates the use of async/await in Python 3.5.
    """


    # Run the asynchronous task
    asyncio.run(main())

def demonstrate_match_case():
    """
    Demonstrates the use of match-case in Python 3.10.
    """

    # Define a variable to match against
    value = 10

    # Use match-case to handle different values
    match value:
        case 10:
            print("Value is 10")
        case 20:
            print("Value is 20")
        case _:
            print("Value is not 10 or 20")

# Define a function that accepts a union type
def greet(name: str | int) -> str:
    """
    Greets the user with a personalized message.

    Args:
        name: The name of the user.

    Returns:
        A greeting message.
    """
    if isinstance(name, str):
        return f"Hello, {name}!"
    else:
        return f"Hello, user {name}!"

def demonstrate_union_operator():
    """
    Demonstrates the use of the union operator (|) in Python 3.10.
    """


    # Call the function with different types of arguments
    print(greet("Alice"))  # Output: Hello, Alice!
    print(greet(123))    # Output: Hello, user 123!

def demonstrate_strict_float_parsing():
    """
    Demonstrates the use of strict float parsing in Python 3.11.
    """

    # Use the strict float parsing behavior in Python 3.11
    try:
        float("1.0e+5")
        print("Strict float parsing successful")
    except ValueError:
        print("Strict float parsing failed")

def demonstrate_new_math_functions():
    """
    Demonstrates the use of new math functions in Python 3.11.
    """

    # Use the new math functions introduced in Python 3.11
    print(f"math.cbrt(8): {math.cbrt(8)}")  # Cube root
    print(f"math.dist([0, 0], [3, 4]): {math.dist([0, 0], [3, 4])}")  # Euclidean distance

if __name__ == "__main__":
    demonstrate_typing()
    demonstrate_lru_cache()
    demonstrate_async_await()
    demonstrate_match_case()
    demonstrate_union_operator()
    demonstrate_strict_float_parsing()
    demonstrate_new_math_functions()
