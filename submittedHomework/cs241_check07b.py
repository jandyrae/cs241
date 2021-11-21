#***********************************************************************
# Program:
#    Checkpoint 07b
#    Brother Parrish, CS241
# Author:
#    Jandy Kiger
# Summary:  work with abstract base method and base class
#***********************************************************************
from abc import ABC
from abc import abstractmethod

class Shape(ABC):
    def __init__(self):
        self.name = ""
    
    def display(self):
        print(f"{self.name} - {self.get_area():.2f}")
    
    @abstractmethod
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.name = "Circle"
        self.radius = 0.0

    def get_area(self):
        return (3.14 * self.radius * self.radius)
        

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.name = "Rectangle"
        self.length = 0.0        
        self.width = 0.0

    def get_area(self):
        return ((self.length) * (self.width))
    

def main():

    shapes = []
    command = ""
    
    while command != "q":
        command = input("Please enter 'c' for circle, 'r' for rectangle or 'q' to quit: ")
        
        if command == "c":
            circle = Circle()
            circle.radius = float(input("Enter the radius: "))
            shapes.append(circle)
        
        elif command == "r":
            rectangle = Rectangle()
            rectangle.length = float(input("Enter the length: "))
            rectangle.width = float(input("Enter the width: "))
            shapes.append(rectangle)

    for shape in shapes:
        shape.display()


if __name__ == "__main__":
    main()

