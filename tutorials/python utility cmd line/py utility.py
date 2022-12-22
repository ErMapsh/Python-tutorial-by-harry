import argparse 
import sys
def calc(args):
    if args.o == 'add':
        return f"addition: {args.x + args.y}"
    
    elif args.o == 'mul':
        return f"mul: {args.x * args.y}"

    elif args.o == 'sub':
        return f"substraction :{args.x - args.y}"

    elif args.o == 'div':
        return f"division: {args.x / args.y}"

    else:
        return "Something Went Wrong"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='sum the integers at the command line')
    
    parser.add_argument('--x', type = float, default=1.0, 
                            help='Enter first no, This is a utility for calculation, plz contact harry bhai')

    parser.add_argument('--y', type = float, default=3.0, 
                            help='Enter second no, This is a utility for calculation, plz contact harry bhai')

    parser.add_argument('--o', type = str, default= "add", 
                            help='Enter second no, This is a utility for calculation, plz contact harry bhai')

    args = parser.parse_args() #Namespace(x=1.0, y=3.0, o='add')
    # print(str(calc(args)))
    sys.stdout.write(str(calc(args)))#u need to print on ps then use that