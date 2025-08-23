"""
Duck Typing in Python

Duck typing is a Pythonic concept where the type or class of an object is less important than the methods and properties it has.
The name comes from the saying:
"If it looks like a duck, swims like a duck, and quacks like a duck, it's probably a duck."

In other words, if an object implements the required behavior, we can use it — regardless of its actual type.

This file demonstrates various aspects of duck typing through multiple examples.
"""

# ===================================
# Example 1: Basic Duck Typing
# ===================================

class Duck:
    def quack(self):
        print("Quack! Quack!")

    def swim(self):
        print("The duck is swimming.")

class Person:
    def quack(self):
        print("I'm pretending to be a duck: Quack!")

    def swim(self):
        print("The person is swimming like a duck.")

class Dog:
    def bark(self):
        print("Woof! Woof!")

    def swim(self):
        print("The dog is swimming.")

# Function that uses duck typing
def make_it_quack_and_swim(creature):
    """
    This function doesn't care about the object's type.
    It only cares that the object has 'quack' and 'swim' methods.
    """
    creature.quack()
    creature.swim()

# ===================================
# Example 2: Duck Typing with Iteration Protocol
# ===================================
class Fibonacci:
    def __init__(self, limit):
        self.prev = 0
        self.curr = 1
        self.limit = limit
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        value = self.prev
        self.prev, self.curr = self.curr, self.prev + self.curr
        self.count += 1
        return value

class CountDown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

def print_sequence(sequence):
    """This function works with any iterable object"""
    print("[", end="")
    print(", ".join(str(item) for item in sequence), end="")
    print("]")

# ===================================
# Example 3: Context Manager Protocol
# ===================================
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"Time taken: {self.end - self.start:.4f} seconds")

class Indenter:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self._indent_write
        self.level = 0
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.original_write
    
    def _indent_write(self, text):
        if text.strip():
            self.original_write('    ' * self.level + text)
        else:
            self.original_write(text)
    
    def indent(self):
        self.level += 1
    
    def dedent(self):
        if self.level > 0:
            self.level -= 1

# ===================================
# Example 4: Duck Typing with len() and str()
# ===================================
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return f"ShoppingCart with {len(self)} items"

class BookShelf:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def __len__(self):
        return len(self.books)
    
    def __str__(self):
        return f"BookShelf containing {len(self)} books"

def print_collection(collection):
    print(f"Collection: {collection}")
    print(f"Number of items: {len(collection)}")

def main():
    # Example 1: Basic Duck Typing
    print("\n" + "="*50)
    print("EXAMPLE 1: BASIC DUCK TYPING")
    print("="*50)
    donald = Duck()
    john = Person()
    buddy = Dog()

    print("=== Duck ===")
    make_it_quack_and_swim(donald)

    print("\n=== Person ===")
    make_it_quack_and_swim(john)

    print("\n=== Dog ===")
    try:
        make_it_quack_and_swim(buddy)  # Will fail because Dog has no 'quack'
    except AttributeError as e:
        print(f"Error: {e}")

    # Example 2: Iteration Protocol
    print("\n" + "="*50)
    print("EXAMPLE 2: ITERATION PROTOCOL")
    print("="*50)
    print("Fibonacci sequence:")
    print_sequence(Fibonacci(10))
    
    print("\nCountdown:")
    print_sequence(CountDown(5))

    # Example 3: Context Manager Protocol
    print("\n" + "="*50)
    print("EXAMPLE 3: CONTEXT MANAGER")
    print("="*50)
    
    print("Timing a block of code:")
    with Timer() as timer:
        # Some time-consuming operation
        total = 0
        for i in range(1000000):
            total += i
    
    print("\nIndentation example:")
    with Indenter() as indent:
        print("Not indented")
        indent.indent()
        print("Indented once")
        indent.indent()
        print("Indented twice")
        indent.dedent()
        print("Back to single indent")

    # Example 4: len() and str()
    print("\n" + "="*50)
    print("EXAMPLE 4: LEN AND STR")
    print("="*50)
    
    cart = ShoppingCart()
    cart.add_item("Laptop")
    cart.add_item("Mouse")
    
    shelf = BookShelf()
    shelf.add_book("Python Cookbook")
    shelf.add_book("Fluent Python")
    shelf.add_book("Clean Code")
    
    print("\nShopping cart:")
    print_collection(cart)
    
    print("\nBookshelf:")
    print_collection(shelf)

if __name__ == "__main__":
    main()