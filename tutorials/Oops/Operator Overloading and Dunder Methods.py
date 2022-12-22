# In Python, we sometimes see method names with double undescore (__), such as __init__ method that every Class has. These methods are called “dunder” methods. In Python, Dunder methods are used for operator overloading and for customizing the behaviour of some other function

#refer Mapping operator to fucntions, there are lots of dunders are there ---------------


class Employe:
    no_of_project_done = 22#class object or variable
    def __init__(self, name, age, skill):#init is constructer 
        self.name = name
        self.age = age
        self.skill = skill

 
    def print_info(self):
        return f"name of member is {self.name} and his age is {self.age}, he know {self.skill}"

    #=================dunders methods
    #Additon 
    def __add__(self, other):
        return f"{self.age + other.age}"

    #substraction
    def __sub__(self, other):
        return f"{self.age - other.age}"

    #float div
    def __truediv__(self, other):
        return other.age/ self.age

    #less than
    def __lt__(self, other):
        return self.age < other.age
    
    #greater than 
    def __gt__(self, other):
        return other.age > self.age

    #absolute object
    def __abs__(self):
        return f"absolute value of Object is {self.age}"

    # a is b
    def is_(self, other):
        return self.age is other.age #return in boolean

    
    #Exponentiation
    def __pow__(self, other):
        return other.age ** 2

    #not equal 
    def __ne__(self, other):
        return f"value of not equal : {self.age !=  other.age}"

    #lots of dunder function are there
  
    def __repr__(self):
        return f"Employe('{self.name}','{self.age}', '{self.skill}')"

    def __str__(self):
        return self.print_info()



emp1 = Employe("ErMapsh", 21, "Programing")
emp2 = Employe("Dr", 25, "claner")

print(emp1 + emp2)
print(emp2 - emp1)
print(emp1 / emp2)
print(emp1 < emp2 )
print(emp1 > emp2 )
print(abs(emp2))
print(emp1 is emp2)
print(emp1)
print(emp1 ** emp2)
print(emp1 != emp2)
print(repr(emp1))#if string dunder function available that time u need to call the fuction using repr method.
print(str(emp1))
print(emp1)
