i = 0;
while i<34:
    if i <= 5:
        i+= 1
        continue;  # continue iteration from starting of the loop, if condition is satisfy
    elif i == 31:
        i+=1
        break;#break the iteration if conditon is satisfy and goes outside of loop
    else:
        print(i, end= " ");
        i+= 1

print()
#assignment
try:
    while True:
        no = int(input("Enter No:"));
        if no<=100:
            continue;
        else:
            print('Number is Enter successfully ..')
            break;


except Exception as e:
    print(e)