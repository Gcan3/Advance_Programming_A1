#setting up a function that calculates the product inside the list
def product(list):
    #setting product as '1' for multiplication process
    prod = 1
    #using for loop to iterate through each values inside the list
    for x in list:
        #values are multiplied by itself until there is no more in the list
        prod = prod * int(x)
    #returning the final product after the iteration
    return prod

#setting up a list
numList = [1,2,3,4,5,6,7,8,9,10]
#invoking the function and passing the list as an argument
#displaying the result
print("The product of the values inside the numList is", product(numList))