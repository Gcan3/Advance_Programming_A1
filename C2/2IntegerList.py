#creating an integer list
intList = [1,3,6,4,9,2,7,5,8,10]
print("The numbers inside the list:")
#displaying the contents of the list using for loop to iterate through each contents inside
for x in intList:
    print(x, end=" ")

print("\nHighest to lowest value in the list:")
#displaying the highest to lowest value of numbers in that list using sort and reversing the sorted list
print(sorted(intList, reverse = True))

#sorting lowest to highest using sort
ascend = sorted(intList)
#[1,2,3,4,5,6,7,8,9,10]

#displaying highest to lowest using sort and reversing the sorted list
descend = sorted(intList, reverse=True)
#[10,9,8,7,6,5,4,3,2,1]

#appending two numbers inside the list
intList.append(11)
intList.append(12)
#displaying the new list
print("Modified list with the two new numbers:")
print(intList)