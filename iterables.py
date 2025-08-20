# python_iterables_demo.py

# 📘 What is an Iterable?
# An iterable is any Python object capable of returning its members one at a time.
# Examples include lists, tuples, strings, dictionaries, sets, and even custom objects.

# ✅ Common Built-in Iterables

# 1. List
my_list = [1, 2, 3, 4]
for item in my_list:
    print("List item:", item)

# 2. Tuple
my_tuple = ('a', 'b', 'c')
for item in my_tuple:
    print("Tuple item:", item)

# 3. String
my_string = "hello"
for char in my_string:
    print("Character:", char)

# 4. Dictionary (iterates over keys by default)
my_dict = {'name': 'Alice', 'age': 30}
for key in my_dict:
    print("Key:", key, "→ Value:", my_dict[key])

# 5. Set
my_set = {10, 20, 30}
for val in my_set:
    print("Set value:", val)


# 🔄 Using `iter()` and `next()` manually

# Convert iterable to iterator
my_iter = iter([100, 200, 300])
print(next(my_iter))  # 100
print(next(my_iter))  # 200
print(next(my_iter))  # 300
# print(next(my_iter))  # Uncommenting this will raise StopIteration


# 🧵 Custom Iterable Class

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            val = self.current
            self.current -= 1
            return val

print("Custom Countdown:")
for num in Countdown(5):
    print(num)


# 🧠 Iterable vs Iterator

# Iterable: Can be looped over (e.g., list, tuple, string)
# Iterator: An object with __next__() method that returns items one at a time

# You can check if an object is iterable using collections.abc
from collections.abc import Iterable, Iterator

print("Is list iterable?", isinstance([1, 2, 3], Iterable))     # True
print("Is list iterator?", isinstance([1, 2, 3], Iterator))     # False
print("Is iter(list) iterator?", isinstance(iter([1, 2, 3]), Iterator))  # True


# 🧪 Generator: A special type of iterator using yield

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Fibonacci sequence:")
for num in fibonacci(7):
    print(num)

# Generators are memory-efficient and lazy-evaluated


# 🔍 Summary:
# - Iterable: Can be looped over (has __iter__)
# - Iterator: Can fetch next item (has __next__)
# - Generators: Elegant way to create iterators using yield
