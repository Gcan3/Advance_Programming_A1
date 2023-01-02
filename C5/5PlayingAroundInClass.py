class Farm():
    #constructor for linking the variables and the object elements
    def __init__(self, Type, Name, Colour, Age, Weight, Noise):
        self.type = Type
        self.name = Name
        self.colour = Colour
        self.age = Age
        self.weight = Weight
        self.noise = Noise
    #method function of printing name
    def hello(self):
        print(f"\nI am {self.name.title()}")
    #method function of making a noise
    def makeNoise(self):
        print(f"{self.noise.upper()}!")
    #method function of printing all the details of the animal
    def animalDetails(self):
        print("\nABOUT ME:")
        print(f"Name: {self.name.title()}\nType: {self.type.title()}\nColour: {self.colour.title()}\nAge: {self.age}\nWeight: {self.weight}\nNoise: {self.noise.title()}")

#Object 1: dog
dog = Farm("dog", "husk", "blue", 5, 23, "woof")
#invoking all of the methods
dog.hello()
dog.makeNoise()
dog.animalDetails()

#Object 2: cow
cow = Farm("cow", "mike", "white", 10, 105, "moo")
#invoking all of the methods
cow.hello()
cow.makeNoise()
cow.animalDetails()