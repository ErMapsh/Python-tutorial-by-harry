#----normal fuction

def normalfucn(a, b , c ):
    print(a, c, b )

normalfucn("Mestri", "Mahesh", "ErMapsh")

# agument sequnece in fucntion is (nomal , *args, **kwargs)
# but is a not right way to implement a fucntion beacuse millions of that function get argument that time fucntion throw error
# using *kwarg and *arg


# ----*Args----
def argfunction(*arg):
    print(arg)
    print(type(arg))
    
argfunction("Mestri", "Mahesh", "ErMapsh")
# data = ["Mestri", "Mahesh", "ErMapsh"]
# argfunction(*data)


# def normal_with_arg(normal , *arg):
#     print(f"first argument is {normal}")
#     for i in arg:
#         if i != arg[-1]:
#             print(f"after first agrument is {i}")
#         else:
#             print(f"Last word in argument is {arg[-1]}")

# normal_with_arg("\"who\"", "the", "fuck", "are", "you", "godddd whree the fuck i mm")




#--------**kwargs-------
def normal_arg_kwargfunc(normal , *args, **kwargs ):
    print(f"nomal agrument: {normal}")
    for i in args:
        print(f"*args arguments: {i}")
    print(kwargs.items())#strored in list here
    for key ,value in kwargs.items():
        print(f"**kwargs arguments: key is {key} & value is {value}")
    
normal_arg_kwargfunc("Student list:", "Where", "The", "Fuck", "I", "Am", **{"Name" : "ErMapsh", "Age" : 21})