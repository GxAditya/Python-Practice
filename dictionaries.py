#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PYTHON DICTIONARIES: COMPREHENSIVE NOTES
========================================

Dictionaries are Python's implementation of a hash table data structure.
Key characteristics:
- Mutable: Can be modified after creation
- Ordered (Python 3.7+)
- Keys must be hashable (immutable types like str, int, tuple)
- Values can be any Python object
- O(1) average case time complexity for lookups
"""

from copy import deepcopy
from pprint import pprint
from collections import defaultdict

# ============================================================================
# 1. DICTIONARY CREATION
# ============================================================================

# Method 1: Using curly braces (most common)
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Method 2: Using dict() constructor
coordinates = dict(x=10, y=20, z=30)  # Keys become strings without quotes

# Method 3: From list of tuples
fruits = dict([("apple", 5), ("banana", 3), ("orange", 7)])

# Method 4: Using dictionary comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Method 5: Using fromkeys() - creates keys with same default value
default_values = dict.fromkeys(["math", "physics", "chemistry"], 100)
# {'math': 100, 'physics': 100, 'chemistry': 100}

# ============================================================================
# 2. ACCESSING AND MODIFYING ELEMENTS
# ============================================================================

# Accessing values
name = person["name"]  # Raises KeyError if key doesn't exist
age = person.get("age")  # Returns None if key doesn't exist
city = person.get("city", "Unknown")  # Returns default if key doesn't exist

# Modifying values
person["age"] = 31  # Update existing key
person["country"] = "USA"  # Add new key-value pair

# Check if key exists
has_name = "name" in person  # True
has_phone = "phone" in person  # False

# Get number of key-value pairs
num_items = len(person)  # 4

# ============================================================================
# 3. DICTIONARY METHODS
# ============================================================================

# Get all keys, values, and items
keys = person.keys()     # dict_keys(['name', 'age', 'city', 'country'])
values = person.values() # dict_values(['Alice', 31, 'New York', 'USA'])
items = person.items()   # dict_items([('name', 'Alice'), ('age', 31), ...])

# Removing items
age = person.pop("age")  # Removes and returns the value for 'age'
person.popitem()         # Removes and returns the last inserted item (Python 3.7+)
person.clear()           # Removes all items

# Copying
shallow_copy = person.copy()  # Creates a shallow copy
deep_copy = deepcopy(person)  # Creates a deep copy

# ============================================================================
# 4. DICTIONARY OPERATIONS (Python 3.9+)
# ============================================================================

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# Merge dictionaries (creates new dict)
merged = d1 | d2  # {'a': 1, 'b': 3, 'c': 4}

# Update in-place
d1 |= d2  # d1 is now {'a': 1, 'b': 3, 'c': 4}

# ============================================================================
# 5. DICTIONARY VIEW OBJECTS
# ============================================================================
"""
keys(), values(), and items() return view objects that provide a dynamic view of
the dictionary's entries. When the dictionary changes, the view reflects these changes.
"""

# Example of dynamic view
person = {"name": "Alice", "age": 30}
keys_view = person.keys()
print("Initial keys:", list(keys_view))  # ['name', 'age']

person["city"] = "New York"
print("After update:", list(keys_view))  # ['name', 'age', 'city']

# ============================================================================
# 6. COMMON DICTIONARY PATTERNS
# ============================================================================

# 1. Counting occurrences of items
text = "hello world"
counter = defaultdict(int)
for char in text:
    counter[char] += 1
print("\nCharacter counts:", dict(counter))

# 2. Grouping with setdefault
people = [
    {"name": "Alice", "department": "Engineering"},
    {"name": "Bob", "department": "Sales"},
    {"name": "Charlie", "department": "Engineering"}
]

department_roster = {}
for person in people:
    department_roster.setdefault(person["department"], []).append(person["name"])
print("\nDepartment roster:", department_roster)

# 3. Dictionary comprehensions with conditions
squared_evens = {x: x**2 for x in range(10) if x % 2 == 0}
print("\nSquares of even numbers:", squared_evens)

# ============================================================================
# 7. IMPORTANT NOTES AND GOTCHAS
# ============================================================================
"""
1. Dictionary keys must be hashable (immutable types like str, int, float, tuple)
2. Dictionaries maintain insertion order in Python 3.7+
3. Be careful with mutable default values
4. Dictionary views are dynamic and reflect changes to the dictionary
5. Use .get() for safe access to avoid KeyError
6. For large dictionaries, consider using dict() instead of {} for better performance
"""

# Example of gotcha with mutable default values
def add_to_letter_counts(letter, counts={}):
    counts[letter] = counts.get(letter, 0) + 1
    return counts

print("\nMutable default gotcha:")
print("First call:", add_to_letter_counts('a'))  # {'a': 1}
print("Second call:", add_to_letter_counts('b'))  # {'a': 1, 'b': 1} - keeps previous values!

# ============================================================================
# 8. DEMONSTRATION
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*80)
    print("DICTIONARY DEMONSTRATION")
    print("="*80)
    
    # Create a sample dictionary
    student = {
        "name": "Alice",
        "age": 22,
        "courses": ["Math", "Physics", "Chemistry"],
        "grades": {"Math": 90, "Physics": 85, "Chemistry": 88}
    }
    
    print("\nStudent record:")
    pprint(student)
    
    # Demonstrate dictionary methods
    print("\nKeys:", list(student.keys()))
    print("Values:", list(student.values()))
    print("Items:", list(student.items()))
    
    # Safe access with get()
    print("\nAccessing non-existent key with get():", student.get("address", "Not provided"))
    
    # Dictionary merging
    new_info = {"age": 23, "address": "123 Main St"}
    updated_student = student | new_info
    print("\nAfter merging with new info:")
    pprint(updated_student)
