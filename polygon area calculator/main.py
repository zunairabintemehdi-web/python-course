from abc import ABC, abstractmethod

# Abstract Base Class (Abstraction)
class Shape(ABC):
    @abstractmethod
    def area(self): pass

# Derived Class: Rectangle (Inheritance)
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self): return self.width * self.height
    def __str__(self): return f"Rectangle({self.width}, {self.height})"

# Derived Class: Square (Inheritance)
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side
    def __str__(self): return f"Square({self.side})"

# Usage Example
if __name__ == "__main__":
    rect = Rectangle(10, 5)
    sq = Square(7)
    print(f"{rect} Area: {rect.area()}")
    print(f"{sq} Area: {sq.area()}")
