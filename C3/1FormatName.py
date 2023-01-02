#getting user input
first = input("Please enter your first name:\n")
last = input("Please enter your last name:\n")

#using f-string to display a neatly formatted text
#using .title() function to capitalize the name
print(f"Hello, {first.title()} {last.title()}")