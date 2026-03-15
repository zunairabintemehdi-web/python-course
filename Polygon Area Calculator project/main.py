# Code 1: Encapsulation & Inheritance (Base Class)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width): self.width = width
    def set_height(self, height): self.height = height
    def get_area(self): return self.width * self.height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

# Code 2: Polymorphism (Derived Class overriding methods)
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    # Polymorphic behavior: setter changes both dimensions
    def set_side(self, side):
        self.width = side
        self.height = side
    
    # Overriding parent method for specific behavior
    def set_width(self, width): self.set_side(width)
    def set_height(self, height): self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"

# Usage Example
rect = Rectangle(10, 5)
sq = Square(5)
print(f"Area: {rect.get_area()}") # Output: 50
print(f"Area: {sq.get_area()}")   # Output: 25
