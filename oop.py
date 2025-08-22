"""
OOP in Python - Tutorial with Examples
--------------------------------------
This file explains the core concepts of Object-Oriented Programming (OOP) in Python:
1. Classes and Objects
2. Attributes and Methods
3. The __init__ Constructor
4. Encapsulation
5. Inheritance
6. Polymorphism
7. Special (Magic/Dunder) Methods
"""

# 1️⃣ DEFINING A CLASS AND CREATING OBJECTS
class Car:
    # Class attribute (shared by all instances)
    wheels = 4

    # Constructor method (called when creating an object)
    def __init__(self, brand, model):
        # Instance attributes (unique to each object)
        self.brand = brand
        self.model = model

    # Instance method (operates on the object)
    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine started.")

    # Instance method with parameters
    def drive(self, speed):
        print(f"{self.brand} {self.model} is driving at {speed} km/h.")

# Creating objects (instances of Car)
car1 = Car("Toyota", "Corolla")
car2 = Car("Tesla", "Model S")

car1.start_engine()
car2.drive(120)

print(f"All cars have {Car.wheels} wheels.\n")


# 2️⃣ ENCAPSULATION (Hiding internal details)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute (name mangling)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Balance: {account.get_balance()}\n")


# 3️⃣ INHERITANCE (Reusing code from a parent class)
class ElectricCar(Car):  # ElectricCar inherits from Car
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)  # Call parent constructor
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"{self.brand} {self.model} is charging to {self.battery_capacity} kWh.")

# Using inherited and new methods
ev = ElectricCar("Tesla", "Model 3", 75)
ev.start_engine()  # Inherited from Car
ev.charge()        # Defined in ElectricCar
print()


# 4️⃣ POLYMORPHISM (Same method name, different behavior)
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Calls the appropriate method for each object
print()


# 5️⃣ SPECIAL METHODS (Magic/Dunder methods)
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __len__(self):
        return self.pages

book = Book("Python 101", "John Doe", 350)
print(book)        # Calls __str__
print(len(book))   # Calls __len__