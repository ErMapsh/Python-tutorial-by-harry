# #parent class ---- child class can access methods, objects of parent class but parent class can't access child class method, objects
# class Employe:
#     # class is made by object, class method, static method, constructer method like __init__(self)
#     no_of_project_done = 22#class object or variable
#     def __init__(self, name, age, skill):#init is constructer 
#         self.name = name
#         self.age = age
#         self.skill = skill
#     @classmethod
#     def changing_member_no(cls, no):
#         cls.no_of_project_done = no
    
#     @staticmethod
#     def print_something(string):
#         print(f"This is {string}")

#     def print_info(self):
#         print(f"name of member is {self.name} and his age is {self.age}, he know {self.skill}")

#     @classmethod
#     def make_simple(cls, string):
#         # params = string.split("-")
#         # # print(params)
#         # return cls(*params)
#         return cls(*string.split("-"))


# #New class (child class) ------ child class can access methods, objects of parent class but parent class can't access child class method, objects
# class Programmer(Employe):
#     no_of_holidays = 45
#     def __init__(self, name, age, skill):
#         self.name = name 
#         self.age = age 
#         self.skill = skill 

#     def print_info_programmer(self):
#         return super().print_info()#copy or using Employe Print_info() print the information.


# ErMapsh = Programmer.make_simple("ErMapsh-21-python")
# ErMapsh.print_info_programmer()
# print(ErMapsh.no_of_holidays)

class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    super().__init__('Dog')
    
d1 = Dog()

