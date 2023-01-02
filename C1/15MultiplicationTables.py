print("Hello, this will print the multiplication table from 1 to 10!")

#making nested for loops to make multiple multiplication tables of each numbers from 1 to 10
#for every numbers from 1 to 10...
for multNum in range(1,11):
    print("The multiplcation table of: ", multNum)
    #...display a product of it when multiplied from 1 to 10
    for multVal in range(1, 11):
        #using f-string to format all numbers and answers
        print(f"{multNum} x {multVal} = {multNum * multVal}")
    #making a new line
    print("")