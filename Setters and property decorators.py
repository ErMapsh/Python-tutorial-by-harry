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



ErMapsh =  Employe("Mahesh", "Mestri")
print(ErMapsh.email)#using Poperty decorator we can run function without brackets
ErMapsh.fname = "Mapsh"
print(ErMapsh.email)#encapsulation concept applied , we dont need to show thing to user

#we want to change the mail using setter
ErMapsh.email = "This.that@ermapsh.com"
print(ErMapsh.email)

#delete fname and lname using email del setter
del ErMapsh.email #delete fname and lname using mail
print(ErMapsh.email)#at this time fname is not avaliable

print()

#new instance
Dr  = Employe("Dr", "Mapsh")
print(Dr.explain())
print(Dr.email)

Dr.email = "Docter.Mapsh@ermapsh.com"
print(Dr.email)

# deleting mail of Dr
del Dr.email
print(Dr.email)