What is your name")
b = input("How much do you earn")
if int(b)==0:
    raise ZeroDivisionError("b is 0 so stopping the program")
if a.isnumeric():
    raise Exception("Numbers are not allowed")