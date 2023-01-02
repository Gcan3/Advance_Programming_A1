#getting user input
print("Hello, in this program it will calculate how many seconds in the days you give!")
days = int(input("Enter the number of days: "))

#turning days into hours, hours to minutes, and minutes to seconds
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

#print the result
print(f"There are {seconds} in {days} day(s)")