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

    @staticmethod #not using class var or instances var, takes arguments only not self, cls
    def good(str):
        print(str, 'is good boy')

adi = Emp("Adi", 21)
adi.details()
adi.good("Adi")