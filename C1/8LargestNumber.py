#collecting user input and converting them to integers
firstNum = int(input("Input the first number: "))
secondNum = int(input("Input the second number: "))
thirdNum = int(input("Input the third number: "))

#multiple if-else gates version
if firstNum > secondNum:
    if firstNum > thirdNum:
        print(firstNum, " is the largest number.")
else:
    if secondNum > thirdNum:
        print(secondNum, " is the largest number.")
    else:
        print(thirdNum, " is the largest number.") 
        
#Ternary version
print(firstNum if firstNum > secondNum and firstNum > thirdNum else secondNum if secondNum > thirdNum else thirdNum, " is the largest number")