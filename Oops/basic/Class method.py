class Emp():
    min_skill = 3

    @classmethod
    def changeSkill(cls, skillno):
        cls.min_skill = skillno

    def __init__(self, Name, Age):# we dont need to add a manually instances of object we can also pass the instances
        self.name = Name
        self.age = Age


    def details(self):
        print(f"The Name is {self.name}, age is {self.age} and he have {self.min_skill} skills")

Mahesh = Emp("Mahesh", 21)# here Self is Mahesh
# Mahesh.details() 

# i want to change his no of skill of Mahesh Object
Mahesh.changeSkill(5)
# Mahesh.details() 




# -----------------------------Class Methods As Alternative Constructors-----------------------------

class Emp1():
    min_skill = 3

    def __init__(self, Name, Age):
        self.name = Name
        self.age = Age

    @classmethod
    def changeSkill(cls, skillno):
        cls.min_skill = skillno

    @classmethod 
    def form_str(cls, str):
        params = str.split("-")
        return cls(params[0], params[1])


    def details(self):
        print(f"The Name is {self.name}, age is {self.age} and he have {self.min_skill} skills")


Karan = Emp1.form_str("Karan-17")
Karan.details()
