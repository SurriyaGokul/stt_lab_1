"""Cleaned version of Assignment 1 Python code.

This file demonstrates corrected code that passes pylint checks.
"""

import os
import math
from typing import Tuple


X = 10
Y = 20


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def safe_divide(a: float, b: float) -> float:
    """Return division result, or 0 if division by zero occurs."""
    if b == 0:
        return 0.0
    return a / b


def shadow_example() -> Tuple[list, str]:
    """Return a list and a string (no shadowing)."""
    items = [1, 2, 3]
    message = "hello"
    return items, message


class Person:
    """A simple class representing a person."""

    def __init__(self, name: str, age: int = 25) -> None:
        """Initialize a person with name and age."""
        self.name = name
        self.age = age
        self.temp = math.sqrt(100)

    def say_hi(self) -> str:
        """Return a greeting message."""
        return f"Hi, my name is {self.name}, I am {self.age} years old."


def main() -> None:
    """Entrypoint for demo."""
    print(add(X, Y))
    print(safe_divide(10, 2))

    items, message = shadow_example()
    print(items, message)

    person = Person("Alice")
    print(person.say_hi())

    cwd = os.getcwd()
    print("Current working directory:", cwd)


if __name__ == "__main__":
    main()
