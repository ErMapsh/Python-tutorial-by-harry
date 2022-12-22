class Emp():

    def __init__(self, Name, Age):# we dont need to add a manually instances of object we can also pass the instances
        self.name = Name
        self.age = Age


    def details(self):
        print(f"The Name is {self.name}, age is {self.age}")



Mahesh = Emp("Mahesh", 21)# here Self is Mahesh
Mahesh.details() 

