print("Hello, this will print the sum of numbers involved you will give!")
#getting user input
num = input("Enter a number: ")

#separating the numbers by converting each string values into integers and adding it to the sum
sum = 0
for x in str(num):
    sum = sum + int(x)
    
#displaying the sum
print("The sum of the numbers inputted is",sum)