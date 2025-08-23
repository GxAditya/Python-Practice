"""
methods_demo.py

This script demonstrates the difference between:
1. Instance Methods
2. Static Methods

We use comments and examples to explain how they work.
"""

class MathOperations:
    # Instance Method
    # ----------------
    # - Takes 'self' as the first parameter.
    # - Can access and modify instance attributes.
    # - Called on an object (instance) of the class.
    def __init__(self, number):
        self.number = number  # instance attribute

    def multiply(self, factor):
        """
        Instance method that multiplies the instance's number by a given factor.
        """
        return self.number * factor

    # Static Method
    # --------------
    # - Defined with @staticmethod decorator.
    # - Does NOT take 'self' or 'cls' as the first parameter.
    # - Cannot access instance (self) or class (cls) attributes directly.
    # - Behaves like a normal function but lives inside the class for logical grouping.
    @staticmethod
    def add(a, b):
        """
        Static method that adds two numbers.
        """
        return a + b


# ---------------------------
# Example Usage
# ---------------------------

# Creating an instance of MathOperations
math_obj = MathOperations(10)

# Calling an instance method
result_instance = math_obj.multiply(5)  # Uses the instance's 'number' (10 * 5)
print(f"Instance Method Result: {result_instance}")  # Output: 50

# Calling a static method
# Can be called on the class itself (no instance needed)
result_static = MathOperations.add(3, 7)
print(f"Static Method Result (via class): {result_static}")  # Output: 10

# Static method can also be called via an instance (not recommended, but possible)
result_static_instance = math_obj.add(2, 4)
print(f"Static Method Result (via instance): {result_static_instance}")  # Output: 6


"""
Key Takeaways:
--------------
1. Instance methods:
   - Require an object to be called.
   - Can access and modify instance attributes.
   - First parameter is 'self'.

2. Static methods:
   - Do not require an object to be called.
   - Cannot access instance or class attributes directly.
   - First parameter is NOT 'self' or 'cls'.
   - Used for utility/helper functions that are related to the class but don't need its data.
"""

"""
magic_methods_demo.py

This script demonstrates Python's "magic methods" (also called dunder methods).
Magic methods:
- Have double underscores before and after their names (e.g., __init__, __str__, __add__).
- Are special hooks that let you define how objects of your class behave in built-in operations.
"""

class Vector:
    def __init__(self, x, y):
        """
        __init__ is the constructor method.
        Called automatically when a new object is created.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        __str__ defines the string representation of the object.
        Called when you use str(obj) or print(obj).
        """
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        """
        __add__ defines the behavior of the '+' operator.
        Called when you do obj1 + obj2.
        """
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __eq__(self, other):
        """
        __eq__ defines the behavior of the '==' operator.
        Called when you compare two objects for equality.
        """
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __len__(self):
        """
        __len__ defines the behavior of the len() function.
        Called when you do len(obj).
        """
        return 2  # This is arbitrary here, just for demonstration.

    def __repr__(self):
        """
        __repr__ defines the 'official' string representation of the object.
        Called in interactive mode or when using repr(obj).
        Should ideally be unambiguous and, if possible, valid Python code.
        """
        return f"Vector(x={self.x}, y={self.y})"


# ---------------------------
# Example Usage
# ---------------------------

v1 = Vector(2, 3)
v2 = Vector(4, 5)

# __str__ in action
print(v1)  # Output: Vector(2, 3)

# __add__ in action
v3 = v1 + v2
print(v3)  # Output: Vector(6, 8)

# __eq__ in action
print(v1 == v2)  # Output: False
print(v1 == Vector(2, 3))  # Output: True

# __len__ in action
print(len(v1))  # Output: 2

# __repr__ in action
print(repr(v1))  # Output: Vector(x=2, y=3)


"""
Key Takeaways:
--------------
1. Magic methods let you customize how your objects behave with Python's built-in functions and operators.
2. Common magic methods:
   - __init__ : Object initialization
   - __str__  : User-friendly string representation
   - __repr__ : Developer-friendly representation
   - __add__  : Addition operator
   - __eq__   : Equality comparison
   - __len__  : Length behavior
3. You can override many more magic methods to control arithmetic, comparisons, iteration, context managers, etc.
"""




"""
class_methods_demo.py

This script demonstrates Python's class methods.

Class methods:
- Are defined with the @classmethod decorator.
- Take 'cls' (the class itself) as the first parameter instead of 'self'.
- Can access and modify class-level attributes.
- Can be called on the class itself or on an instance.
"""

class Employee:
    # Class attribute (shared by all instances)
    company_name = "TechCorp"
    employee_count = 0

    def __init__(self, name):
        """
        __init__ is an instance method (constructor).
        It sets instance attributes and updates the class attribute.
        """
        self.name = name
        Employee.employee_count += 1

    # Class Method
    # ------------
    # - Defined with @classmethod.
    # - First parameter is 'cls', which refers to the class itself.
    # - Can access and modify class attributes.
    @classmethod
    def set_company_name(cls, new_name):
        """
        Updates the company_name for all employees.
        """
        cls.company_name = new_name

    @classmethod
    def get_employee_count(cls):
        """
        Returns the total number of employees created.
        """
        return cls.employee_count

    @classmethod
    def from_string(cls, employee_str):
        """
        Alternative constructor:
        Creates an Employee object from a 'Name' string.
        """
        name = employee_str.strip()
        return cls(name)


# ---------------------------
# Example Usage
# ---------------------------

# Creating employees using the normal constructor
emp1 = Employee("Alice")
emp2 = Employee("Bob")

# Creating an employee using the alternative constructor (class method)
emp3 = Employee.from_string("Charlie")

# Accessing class method to get employee count
print(f"Total Employees: {Employee.get_employee_count()}")  # Output: 3

# Changing company name using class method
Employee.set_company_name("NextGen Solutions")

# All instances see the updated company name
print(emp1.company_name)  # Output: NextGen Solutions
print(emp2.company_name)  # Output: NextGen Solutions
print(emp3.company_name)  # Output: NextGen Solutions


"""
Key Takeaways:
--------------
1. Class methods:
   - Use @classmethod decorator.
   - First parameter is 'cls' (the class itself).
   - Can access and modify class-level data.
   - Can be called on the class or an instance.
   - Often used for alternative constructors or operations affecting the whole class.

2. Difference from instance methods:
   - Instance methods work with object-specific data (self).
   - Class methods work with class-wide data (cls).

3. Difference from static methods:
   - Static methods don't take 'self' or 'cls'.
   - Class methods take 'cls' and can modify class state.
"""