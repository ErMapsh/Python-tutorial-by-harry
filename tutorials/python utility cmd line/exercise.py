#faulty calculater
# 45*3 = 555, 56+9 =77, 56/6=4 
import argparse
import sys

def calc(arg):
    if args.o == 'add':
        if arg.a == 56 and arg.b == 9:
            return f"addition of your number is 77"
        else: 
            return f"addition of your number is {arg.a + arg.b}"

    elif arg.o == 'mul':
        if arg.a == 45 and arg.b == 3:
            return f"mul of your number is 555"
        else: 
            return f"mul of your number is {arg.a * arg.b}"

    elif arg.o == 'div':
        if arg.a == 56 and arg.b == 6:
            return f"div of your number is 4"
        else: 
            return f"div of your number is {arg.a / arg.b}"

    elif arg.o == 'sub':
        return f"sub of your number is {arg.a - arg.b}"
    else:
        return "Something Went Wrong.."


    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    #u can now add new cmd in ur program
    parser.add_argument('--a', type = int, default= 4, help= 'bc mahesh kde ja')
    parser.add_argument('--b', type = int, default= 5, help= 'bc mahesh kde ja')
    parser.add_argument('--o', type = str, default= 'add', help = 'bc kahi pn kr but perfect kr, nahi tr zv bayek' )


    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))#default value getting if u run this file , u need to use command line to use differnt value