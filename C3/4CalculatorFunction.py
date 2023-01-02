#setting the functions and its operations
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
def modulus(num1, num2):
    return num1 % num2

#getting user input first
x = float(input('Enter the first number: '))
y = float(input('Enter the second number: '))
#giving options for user to choose
op = int(input("Choose your operation \n1 Add\n2 Subtract\n3 Multiply\n4 Divide\n5 Modulus\n\n="))
#using if gates based on users operation of choice
#displays the output immediately based on the two numbers entered earlier
if op == 1:
    print("The two numbers you chose and the operation addition the result is: ", add(x, y))
elif op == 2:
    print("The two numbers you chose and the operation subtraction the result is: ", subtract(x,y))
elif op == 3:
    print("The two numbers you chose and the operation multiplication the result is: ", multiply(x,y))
elif op == 4:
    print("The two numbers you chose and the operation division the result is: ", divide(x,y))
elif op == 5:
    print("The two numbers you chose and the operation modulus the result is: ", modulus(x,y))
else:
    print("Error input, please restart the program.")