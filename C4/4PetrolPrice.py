#making two empty lists
petrol = []
price = []

#opening the text file
with open("petrolPrice.txt") as file_handler:
    #storing each lines of the file into a variable
    lines = file_handler.readlines()

#using for loops to iterate through each line
#the objective is to: 1. split the values(words and numbers) and turn it as one
#2. To get their index value and add it into their respective list
for pvalue in lines:
    petrol.append(pvalue.split()[0])
for cvalue in lines:
    price.append(cvalue.split()[1])
    
#using .remove() function to remove the labels of each column stored in a list
petrol.remove("Liters")
price.remove("cost")

below = []
totalpetrol = 0
totalprice = 0
#iterate through the lists contents which is parallel to each other
for x, y in zip(petrol, price):
    #divide the price by the petrol for each row
    totalpetrol = totalpetrol + float(x)
    totalprice = totalprice + float(y)
    #including the calculation of of each rows (the price to the petrol)
    result = round(float(y) / float(x), 1)
    #if the quotient is less than 3.5, add it to the list of "3.5 below liters"
    if result < 3.5:
        below.append(x)

#calculating the average by getting the total price divided by the total petrol
avg = totalprice / totalpetrol

#printing the overall average price per liter
print("The average price per litre of petrol bought",round(avg, 1))

#displaying the list of "3.5 below liters"
print("The petrol in litres that were bought at under 3.5AED per liter are:")
for x in below:
    print(x)