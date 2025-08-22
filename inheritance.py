"""
Inheritance in Python - Tutorial with Examples
----------------------------------------------
This file covers:
1. What is Inheritance?
2. Types of Inheritance:
   - Single Inheritance
   - Multiple Inheritance
   - Multilevel Inheritance
   - Hierarchical Inheritance
3. The super() keyword
"""

# 1️⃣ SINGLE INHERITANCE
# One child class inherits from one parent class

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Inherited method
dog.bark()   # Own method
print()


# 2️⃣ MULTIPLE INHERITANCE
# A child class inherits from more than one parent class

class Flyer:
    def fly(self):
        print("Can fly")

class Swimmer:
    def swim(self):
        print("Can swim")

class Duck(Flyer, Swimmer):  # Duck inherits from both Flyer and Swimmer
    def quack(self):
        print("Duck quacks")

duck = Duck()
duck.fly()
duck.swim()
duck.quack()
print()


# 3️⃣ MULTILEVEL INHERITANCE
# A class inherits from a child class which itself inherits from another class

class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):  # Car inherits from Vehicle
    def drive(self):
        print("Car drives")

class ElectricCar(Car):  # ElectricCar inherits from Car
    def charge(self):
        print("ElectricCar charges")

ev = ElectricCar()
ev.move()
ev.drive()
ev.charge()
print()


# 4️⃣ HIERARCHICAL INHERITANCE
# Multiple child classes inherit from the same parent class

class Shape:
    def area(self):
        print("Calculating area")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

circle = Circle()
square = Square()
circle.area()
circle.draw()
square.area()
square.draw()
print()


# 5️⃣ USING super() TO ACCESS PARENT METHODS
# super() is used to call methods from the parent class

class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)  # Call parent constructor
        self.student_id = student_id

    def show(self):
        super().show()  # Call parent method
        print(f"Student ID: {self.student_id}")

student = Student("Alice", "S123")
student.show()