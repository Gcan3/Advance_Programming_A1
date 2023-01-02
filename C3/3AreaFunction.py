#setting up the functions for area calculations
#circle area function
def circ(radius):
    PI = 3.14159
    area = radius * radius * PI
    return area
#square area function
def square(side):
    area = side * side
    return area
#triangle area function
def tri(base, height):
    area = (height * base) / 2
    return area

#present a menu for the user to choose
print("Hello user, please choose wether you want to calculate the area of:\n1 Circle\n2 Square\n3 Triangle")
selection = input("= ")
#setting an if gate for the user's selection
#all conditions under the if gates contains function calling and outputting the result based on the input of measurement
if selection == "1":
    print("You chose to calculate the area of a circle.")
    radius = int(input("Please enter the radius of the circle:\n"))
    print(f"The area of the circle with the radius of {radius} is {circ(radius)}")
elif selection == "2":
    print("You chose to calculate the area of a square.")
    side = int(input("Please enter the length of a side of the square:\n"))
    print(f"The area of the square with the side length of {side} is {square(side)}")
elif selection == "3":
    print("You chose to calculate the area of a triangle.")
    base = int(input("Please enter the base length of the triangle:\n"))
    height = int(input("Please enter the height of the triangle:\n"))
    print(f"The area of the triangle with the base of {base} and the height of {height} is {tri(base,height)}")
else:
    print("Error in the input, please restart the program.")