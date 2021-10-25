# faulty calculater for who cheating in exam and following calculation are ask in exam so
# they will use calculater so ans will be getting wrong for  theme
# 45*3 = 555, 56+9 = 77, 56/6 = 4

try:
    first_no = int(input('Enter The first no:'));
    second_no = int(input('Enter The second no:'));

    print("1.addition\n2.substraction\n3.multiplication\n4.divide");
    choice = int(input("Enter Your Choice:"));

    # for addition
    if choice == 1 and first_no == 56 and second_no == 9:
        print("Addition of no: 77");
    elif choice == 1:
        print("Addition of no:", first_no + second_no);

    # for substraction
    elif choice == 2:
        print("Substraction of no:", first_no - second_no);

    # for mul
    elif choice == 3 and first_no == 45 and second_no == 3:
        print("Multiplication of no: 555")
    elif choice == 3:
        print("Multiplication of no:", first_no * second_no)


    # for division
    elif choice == 4 and first_no == 56 and second_no == 4:
        print("Division of no: 4");
    elif choice == 4:
        print("Division of no:", first_no / second_no);

    else:
        print("Wrong Choice...")



except Exception as e:
    print("Please, Enter numbers in digit")