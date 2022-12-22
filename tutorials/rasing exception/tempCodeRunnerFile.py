("Enter your name")
try:
    print(c)

except Exception as e:

    if c =="harry":
        raise ValueError("Harry is blocked he is not allowed")

    print("Exception handled")