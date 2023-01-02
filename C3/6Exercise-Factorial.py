#making a recursive function to find the factorial of a number
def fact(n):
    #if the number the user entered is 1, then it will return as 1 (because 1! = 1)
    if n == 1:
        return 1
    #otherwise, the function will repeat with a decremented value argument
    else:
        return (n * fact(n - 1))

#getting user input
i = int(input("Enter number to find its factorial: "))
#displaying the factorial by calling it with the user's input as argument
print(f"The factorial of {i} is {fact(i)}")