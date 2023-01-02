class Employee:
    #constructor function
    def __init__(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary
    #method function for setting user's input data
    def setData(self):
        return self.name, self.age, self.id, self.salary
    #method function for displaying the data
    def getData(self):
        for x in emp_object:
            #calling the index of the tuples and display them properly without the brackets and commas
            #using tab spacing for better visualization
            print(f"{x[0]}\t\t{x[1]}\t{x[2]}\t{x[3]}")
#creating an empty list to store tuples of employees' information
#making one tuple solely for the labels for output purposes
emp_object = [("Name", "Age", "ID", "Salary")]
#iterate through a loop 5 times for the user to make input for 5 employees
for i in range(1,6):
    print("Details for employee number", i, ":")
    name = input("Enter employee's name: ")
    age = input("Enter employee's age: ")
    id = input("Enter employee's id: ")
    salary = input("Enter employee's salary: ")
    #make an object and link it to the class every loop
    myEmployee = Employee(name.title(), age, id.upper(), salary)
    #and append the stored data by calling the setData() function outside the class
    emp_object.append(myEmployee.setData())
#getting the output from the object of the class through the display method
print("\nEmployee data chart:")
myEmployee.getData()