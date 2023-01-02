print("Hello, this will print details of you from you!")
#getting information from the user
name = input('Enter your name: ')
#converting string input of the user into integer value
age = int(input('Enter your age: '))
hometown = input('Enter your hometown: ')

#printing the users inputs into one single print syntax using f-string
#including .title to capitalize the first letter of the user's inputs
print(f"\n\nYour name: {name.title()} \nYour age: {age} \nYour hometown: {hometown.title()}")