class A:
    def met(self):
        print("This is a method from Class A")

class B(A):
    def met(self):
        print("This is a method from Class B")

class C(A):
    def met(self):
        print("This is a method from Class C")

class D(C, B):#order of class in multiple inheritance matter
    pass


a = A()
b = B()
c = C()
d = D()

d.met()