"""
operations.py

This file contains ALL calculator operations that the team will build.

IMPORTANT:
- All developers work in THIS SAME FILE.
- Each developer completes ONLY their own function.
- You are NOT allowed to move your function to a different file.

This shared file is intentional. You will probably create merge conflicts.
That's part of the exercise.
"""

def format_result(result):
    return f"{result}"

def add(a, b):
    """Return the sum of a and b. Developer A owns this function."""
    return (a+b)


def sub(a, b):
    """Return a minus b. Developer B owns this function."""
    result = a - b
    return format_result(result)


def mul(a, b):
    """Return the product of a and b. Developer C owns this function."""
    return (a*b)


def div(a, b):
    """Return a divided by b. Developer D owns this function."""
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: Can't divide by zero"