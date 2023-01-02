#creating an empty list
numList = []
#getting user input through for loop (looping 5 times to get 5 numbers)
print("Hello user, this is to print a list of the five numbers you inputted!")
for x in range(5):
    num = int(input("Enter a number:"))
    #adding the user's input into the list using .append() with the num parameter
    numList.append(num)
#printing the modified list
print("This is the list of the numbers you inputted:\n",numList)