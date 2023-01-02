#getting user input
print("Hello, this program will calculate if this is a triangle or not")
a = int(input("Enter the length of the first side of the triangle: "))
b = int(input("Enter the length of  the second side of the triangle: "))
c = int(input("Enter the length of the remaining side of the triangle: "))

#making "if" gates to determine its possibility
if c <= a + b:
    print("With the side you entered, that is verified to be a triangle!")
    #CODE FOR BONUS PROBLEM
    #nesting an "if" gate to determine what type of triangle it is
    if a == b == c:
        print("And this triangle is considered to be equilateral!")
    elif a == b or a == c or b == c:
        print("And this is considered to be an isosceles!")
    else:
        print("And this is considered to be scalene due to different lengths")
else:
    print("That is not a triangle unfortunately")