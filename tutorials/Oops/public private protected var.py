# --------------------access specifier-----------------------
# Public var - in this anyone can see class object 
# protectd var - in this specific entities can see class object ie. variable like _protectdVariable
# private var  - only for that person who write that

class Employe:
    # class is made by object, class method, static method, constructer method like __init__(self)
    _ProtectedVariable = "ErMapsh"
    __privateVariable = "Fuck You"
    no_of_project_done = 22#class object or public variable

    def __init__(self, name, age, skill):#init is constructer 
        self.name = name
        self.age = age
        self.skill = skill
    @classmethod
    def changing_member_no(cls, no):
        cls.no_of_project_done = no
    
    @staticmethod
    def print_something(string):
        print(f"This is {string}")

    def print_info(self):
        print(f"name of member is {self.name} and his age is {self.age}, he know {self.skill}")

    @classmethod
    def make_simple(cls, string):
        # params = string.split("-")
        # # print(params)
        # return cls(*params)
        return cls(*string.split("-"))

#intance of Employe class
ErMapsh = Employe("ermapsh", 21, "python")
print(ErMapsh.no_of_project_done)
print(ErMapsh._ProtectedVariable)
print(ErMapsh._Employe__privateVariable)#for accessing private variable need to use [ _ClassName__variableName] to print, beacause python save private variable as _ClassName__variable 
