# polymorphism_demo.py

import math

class Shape:
    """A base class representing a generic shape."""
    
    def area(self):
        """Placeholder method to calculate the area of a shape."""
        raise NotImplementedError("Subclasses must override this method")

class Rectangle(Shape):
    """A class representing a rectangle."""
    
    def __init__(self, length, width):
        """Initialize a rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """A class representing a circle."""
    
    def __init__(self, radius):
        """Initialize a circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)
