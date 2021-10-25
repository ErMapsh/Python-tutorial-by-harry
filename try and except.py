try:
    a = int(input("Enter First no:"))
    b = int(input("Enter Second no:"))
    print("average of two no:", a+b/2 )
except Exception as e:
    print(e)