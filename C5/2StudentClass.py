class Students:
    #constructor of the class
    #initializes the variables
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    #method of calculation function
    def calcGrade(self):
        avg = (self.mark1 + self.mark2 + self.mark3) / 3
        #return the rounded average
        return round(avg, 1)
    #method of display function
    def display(self):
        #calling the function inside the class
        print(f'The average grade of student {self.name.title()} is {self.calcGrade()}')

#getting user input
print("Hello user, please enter the appropriate details:")
name = input("Enter the student name: ")
mark1 = int(input(f"Enter the English marks of {name.title()}: "))
mark2 = int(input(f"Enter the Math marks of {name.title()}: "))
mark3 = int(input(f"Enter the History marks of {name.title()}: "))

#create an object based on the user's input
student1 = Students(name, mark1, mark2, mark3)
#display the average based on the user's input by calling the display method outside of the class
student1.display()