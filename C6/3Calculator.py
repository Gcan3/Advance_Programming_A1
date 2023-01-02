#importing the operator into a simple invocation key
import operator as op
#displaying the menu to the user
print("Greetings user, welcome to the calculator program.\nWe offer a list of functions:")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus\n6. Check greater number")
#begin iteration immediately
while True:
    #ask the user input and store it in a variable which will be used later
    userInput = input("Please choose what function you would like to use based on their numbers:")
    #if-gates to check if the input is a digit, otherwise continue the loop
    if userInput.isdigit():
        #nested if-gate to see if the input is within the given choices (1 to 7)
        #before verifying, it is needed to be changed into a literal integer
        #this is to be eligible for range checking
        if int(userInput) in range(1,7):
            #Reconvert the input back to string and break the loop
            str(userInput)
            break
        else:
            #If it does not satisfy the given, continue the loop
            print("Error, number inputted is either below or above the given choices")
            continue
    else:
        print("Incorrect input. Please try again.")
        continue

#Functions with their specified operator module functions
#These functions only have one parameter which is the list of integers
def add(list):
    sum = 0
    for x in list:
        sum = op.add(sum,x)
    return sum
def sub(list):
    diff = list[0] 
    #making a negative index to go through the list
    #this is to iterate through each values which would otherwise be error
    n_indx = -(len(list) - 1) 
    #for every variables inside the range of the list's length minus 1,
    for x in range(len(list) - 1):
        #subtract the first value with its negative index 
        #example: in a list of [1,2,3]
        #first iteration would be op.sub(1, list[-2])
        diff = op.sub(diff, list[n_indx])
        #after the calculation, add the index by one to reach till the last index of the list
        n_indx += 1
    #return the final result
    return diff
def mul(list):
    prod = 1
    for x in list:
        prod = op.mul(x,prod)
    return prod
def div(list):
    quot = list[0]
    for x in list:
        #using true division in the case for when the output < 1
        quot = op.truediv(quot,x)
    return quot
def mod(list):
    #modulo series is also the same as subtraction's case
    remain = list[0]
    n_indx = -(len(list) - 1)
    for x in range(len(list) - 1):
        diff = op.mod(remain, list[n_indx])
        n_indx += 1
    return diff
def gt(list):
    #using the first index of the list as the greatest number
    lnumber = list[0]
    #iterating through the list
    for number in list:
        #if that number is larger than the largest number (currently [0]),
        if op.gt(number, lnumber):
            #declare the largest number into that
            lnumber = number
    #return that largest number
    return lnumber

#empty list to store all of the user's integers
numVals = []

#activate the second loop 
while True:
    #ask for user's input
    usrInpt = input("Please enter a value or press q to quit: ")
    #using same verification gate for checking the inputs of the user
    #first is to checkout the special characters
    if usrInpt.isalnum(): 
        #second is to check if the input is string, otherwise append the input into the list
        if usrInpt.isalpha():
            #third is where if the input is the break key or not, which will continue the loop if not
            if usrInpt == "q" or usrInpt == "Q":
                break
            else:
                print("Invalid input. Try again.")
                continue
        else:
            numVals.append(int(usrInpt)) #converting it into integer value to be calculable
            continue
    else:
        print("Incorrect input. Please try again.")
        continue

#convert the first user input into integer so that it can be used on the series of if-gates
userInput = int(userInput)
#in each gates, they call out the function with the number list as the parameter
#it will display the returned value from those functions
if userInput == 1:
    print("You chose to add the numbers and the result is:")
    print(add(numVals))
elif userInput == 2:
    print("You chose to subtract with the numbers and the result is:")
    print(sub(numVals))
elif userInput == 3:
    print("You chose to multiply the numbers and the result is:")
    print(mul(numVals))
elif userInput == 4:
    print("You chose to divide with the numbers and the result is:")
    print(div(numVals))
elif userInput == 5:
    print("You chose to find the modulo with the numbers and the result is:")
    print(mod(numVals))
elif userInput == 6:
    print(f"The largest number is {gt(numVals)}")

#finishing message
print("Thank you")