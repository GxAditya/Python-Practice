# function_arguments_demo.py

# 📌 1. Positional Arguments
# These are the most common type. The order of arguments matters.

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Alice", 30)  # Output: Hello Alice, you are 30 years old.


# 📌 2. Keyword Arguments
# You specify the parameter name explicitly, so order doesn't matter.

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(pet_name="Buddy", animal_type="dog")  # Output: I have a dog named Buddy.


# 📌 3. Default Arguments
# You can assign default values to parameters. These are used if no value is provided.

def power(base, exponent=2):
    print(f"{base} raised to the power of {exponent} is {base ** exponent}")

power(5)           # Uses default exponent=2 → Output: 25
power(5, 3)        # Overrides default → Output: 125


# 📌 4. Variable-Length Arguments (*args)
# Use *args to pass a variable number of non-keyword arguments.

def sum_all(*numbers):
    total = sum(numbers)
    print(f"Sum of numbers: {total}")

sum_all(1, 2, 3)           # Output: 6
sum_all(10, 20, 30, 40)    # Output: 100


# 📌 5. Variable-Length Keyword Arguments (**kwargs)
# Use **kwargs to pass a variable number of keyword arguments.

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="Delhi")
# Output:
# name: Alice
# age: 30
# city: Delhi


# 📌 6. Combination of All Types
# You can combine all types, but the order must be:
# positional → *args → default → **kwargs

def full_example(a, b, *args, c=10, **kwargs):
    print(f"a: {a}, b: {b}, c: {c}")
    print("args:", args)
    print("kwargs:", kwargs)

full_example(1, 2, 3, 4, 5, c=20, x=100, y=200)
# Output:
# a: 1, b: 2, c: 20
# args: (3, 4, 5)
# kwargs: {'x': 100, 'y': 200}