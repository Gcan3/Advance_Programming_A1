#making a function for adding two integers
def add(num1, num2):
    return num1 + num2

#getting user input
x = int(input("Enter the first number:\n"))
y = int(input("Enter the second number:\n"))

#display the sum by calling the add function with the user's inputs as arguments
print(f"The sum of {x} and {y} is {add(x,y)}")