class Employe:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}.{self.lname}@ermapsh.com"
    
    def explain(self):
        return f"This Employe is {self.fname} {self.lname}"

    @property #decorator
    def email(self):
        if self.fname == None or self.lname == None:
            return "email not set.., please using setter"
        return f"{self.fname}.{self.lname}@ermapsh.com"

    @email.setter #setter
    def email(self, string):
        print("Setting Now..............")
        names = string.split("@") [0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
        return self.fname, self.lname


    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skillF = Employe("Er", "Mapsh")
print(skillF.explain())
print(type(skillF))

print(id("that that"))
print(id("that that1"))

#what thing in a that
print(dir(skillF))




import inspect
print(inspect.getmembers(skillF))
print(inspect.ismodule(inspect))
print(inspect.ismethod(skillF.explain))