def cal(arg, sems):
    sum = 0
    for i in arg:
        sum += i 
    return sum/sems

if __name__ == "__main__":
    ls = []
    semister = int(input("Enter Total Sem no: "))
    for i in range(1, semister+1):
        ls.append(float(input(f"Enter the pointer of sem {i}: ")))
    print(f"your cgpa of {semister} sems is {cal(ls, semister)}")


