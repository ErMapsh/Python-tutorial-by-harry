#harry have n no of apples, he have some student, he want to distributes the apple. these n number of apples are provided to harry by his friends, he can request few less or few more apples


student_no = int(input("Enter the no of students:"))
min_app = int(input("Enter the minimum no of apples:"))
max_app = int(input("Enter the maximun no of apples:"))

if min_app != max_app:
    for i in range(min_app, max_app+1):
        if  i % student_no == 0:
            print(f"{i} is divisor of {student_no}")
        else:
            print(f"{i} is not divisor of {student_no}")
else:
    print("minimum and maximum value are same, its gone wrong")
