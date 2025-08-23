from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        print(f"This is a {self.__class__.__name__}.")

# Concrete subclass: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Concrete subclass: Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Driver code
def main():
    shapes = [
        Circle(radius=5),
        Rectangle(width=4, height=6)
    ]

    for shape in shapes:
        shape.describe()
        print(f"Area: {shape.area():.2f}")
        print(f"Perimeter: {shape.perimeter():.2f}")
        print("-" * 30)

if __name__ == "__main__":
    main()