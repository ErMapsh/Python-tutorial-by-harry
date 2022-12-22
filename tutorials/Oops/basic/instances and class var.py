class Student():
   no_of_student= 211

Mahesh = Student() # Its begin a object of Student class
ErMapsh = Student() # Its begin a object of Student class


print(Student.__dict__)
ErMapsh.no_of_student = 21 # Create new instance varible 
print("--->",ErMapsh.__dict__)

ErMapsh.no_of_student = 34 # When i change no of student , is create new instance var for that object
print("changing--->",ErMapsh.__dict__)

# We cant change Class var using object but we can like this
print("no of student:",Student.no_of_student)
Student.no_of_student = 4
print("no of student changings:",Student.no_of_student)