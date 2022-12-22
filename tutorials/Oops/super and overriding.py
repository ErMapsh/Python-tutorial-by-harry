class A:
    classvar1 = "I am class variable in Class A"
    slogan = "Fuck the world"
    def __init__(self):
        self.var1 = "I am in a constructer A"
        self.classvar1 = "i m a instance classVar1 in A"
        self.special = "special variable"

class B(A):
    classvar1 = "I am in class varible in Class B"
    def __init__(self):
        self.var1 = "I am in a constructer in B"
        self.classvar1 = "i m a instance classVar1 in B"
        super().__init__()#abhi yaha pe var1 aur classvar1 class A ka access hoga, cause class B ke variable override honge
        super().classvar1




a = A()
b = B()
print(b.classvar1)
print(b.var1)
print(b.special)
print(b.classvar1)