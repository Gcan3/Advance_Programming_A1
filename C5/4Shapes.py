#super class
class Shapes:
    def __init__(self, side1, side2, side3):
        self.base = side1
        self.side2 = side2
        self.height = side3
    def inputSides():
        base = int(input("Input the base length of a side/radius (for all shapes): "))
        side2 = int(input("Input the second side (for rectangle): "))
        height = int(input("Input the third side/height (for triangle): "))
        return Shapes(base, side2, height)
#sub class
class Circle(Shapes):
    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)
    def area(self):
        print((self.base * self.base) * 3.14)
#sub class
class Rectangle(Shapes):
    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)
        
    def area(self):
        print(self.base * self.side2)
#sub class
class Triangle(Shapes):
    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)
    
    def area(self):
        print(round((self.base * self.height) / 2, 1))

#making an object for getting the information
side = Shapes.inputSides()
#distributing the object information to other objects that calculates their respective area
#for circle
print("Circle area:")
circleArea = Circle.area(side)
#for rectangle
print("Rectangle area:")
rectangleArea = Rectangle.area(side)
#for triangle
print("Triangle area:")
triangleArea = Triangle.area(side)