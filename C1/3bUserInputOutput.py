#introduce and get information from the user
print("Hello, user!")
name = input("What is your name?\n")
age = int(input("What is your age?\n"))

#printing the name of the user, length of the name, and the age of the user after one year
print("\nIt is good to meet you", name.title())
#subtracting the length with the number of spaces to exclude into the length count
print("The length of your name is", len(name) - name.count(" "))
print("Your age next year will be", age + 1)