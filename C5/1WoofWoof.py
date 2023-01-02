#making a class Dog
class Dog:
    #assigning data members to the class constructor 
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    #method function of displaying the objects' given data
    def display(self):
        print(f'\nDetails of {self.name.title()} the dog is:')
        print('Name:', self.name.title())
        print('Breed:', self.breed.title())
        print('Age:', self.age, 'years old')
    #method of printing the oldest dog
    def oldest(self):
        print(f'\nThe oldest dog is {self.name.title()} with the age of {self.age}')

#object 1
myDog = Dog("marley", "golden retriever", "3")
#calling the display function outside of the class
myDog.display()
#object 2
myDog2 = Dog("husk", "husky", "5")
#calling the display function outside of the class
myDog2.display()
#using if gates to determine if the first object is older than the second or vice-versa
#then calling the "oldest()" function outside the class
if myDog.age > myDog2.age:
    myDog.oldest()
else:
    myDog2.oldest()