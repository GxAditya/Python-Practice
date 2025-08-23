"""
decorators_demo.py

This script demonstrates:
1. Function decorators (custom and built-in)
2. The @property decorator (and its setter)

Decorators:
-----------
- A decorator is a function that takes another function (or method) as input,
  adds extra functionality to it, and returns a new function.
- They are applied using the '@decorator_name' syntax above a function definition.

@property:
--------
- A special built-in decorator for turning a method into a "read-only" attribute.
- Often used for computed attributes.
- Can be paired with a setter method to allow controlled modification.
"""

# ---------------------------
# 1. Function Decorator Example
# ---------------------------

def debug_decorator(func):
    """
    A simple decorator that logs the function name and arguments before calling it.
    """
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[DEBUG] {func.__name__} returned {result}")
        return result
    return wrapper

@debug_decorator
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

@debug_decorator
def greet(name):
    """Returns a greeting message."""
    return f"Hello, {name}!"


# ---------------------------
# 2. @property Decorator Example
# ---------------------------

class Rectangle:
    def __init__(self, width, height):
        self._width = width      # underscore to indicate "private" attribute
        self._height = height

    @property
    def area(self):
        """
        @property makes this method accessible like an attribute:
        rect.area instead of rect.area()
        """
        return self._width * self._height

    @property
    def width(self):
        """Getter for width."""
        return self._width

    @width.setter
    def width(self, value):
        """
        Setter for width.
        Allows controlled modification of the private _width attribute.
        """
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        """Getter for height."""
        return self._height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value


# ---------------------------
# Example Usage
# ---------------------------

# Function decorators in action
print(add(3, 5))
print(greet("Alice"))

# @property in action
rect = Rectangle(4, 5)
print(f"Area: {rect.area}")  # Access like an attribute, not a method

# Using setters
rect.width = 10
rect.height = 6
print(f"Updated Area: {rect.area}")

# Attempting to set invalid value
try:
    rect.width = -2
except ValueError as e:
    print(f"Error: {e}")


"""
Key Takeaways:
--------------
1. Function decorators:
   - Wrap and enhance functions without modifying their code.
   - Syntax: @decorator_name above the function definition.
   - Can be stacked for multiple layers of functionality.

2. @property decorator:
   - Turns a method into a read-only attribute.
   - Can be paired with @<property>.setter to allow controlled updates.
   - Useful for computed attributes or encapsulating validation logic.

3. Decorators are a powerful way to keep code DRY, reusable, and expressive.
"""