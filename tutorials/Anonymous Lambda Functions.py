#normal way to define a function
def add(x, y):
    return x+y

add(4, 3)

#write a function using new way
addition = lambda x, y: x+y#lambda dont return
print(addition(3, 1))


no = [(4, 22, 1, 5, 3)]
no.sort(key=lambda x: print(x[2:]))#working on grout not on int