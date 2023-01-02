print("Hello, this will print the circumference and the area of the circle with your given radius!")
#setting up a constant by making the variable name all capitals
PI = 3.14159
radius = int(input('Enter radius of the circle: '))
circum = PI * radius * 2
area = PI * radius * radius

print('The circumference of the circle with the radius you entered is', circum)
print('The area of the circle with the radius you entered is', area)