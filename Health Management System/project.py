# Health Management System
# 3 client  - harry, Rohan, ErMapsh total 6 files

def getdate():
    import datetime
    return datetime.datetime.now()

def exercise(a):
    with open(f"{a} Exercise", "a+") as f:
        info = input("What Client Exercise did?:")
        f.write(f"{getdate()}: {info}\n")

def diet(b):
    with open(f"{b} Diet", "a+") as f:
        info = input("What Client eat?:")
        f.write(f"{getdate()}: {info}\n")


def ui():
    client_names = set(("harry", "Rohan", "ErMapsh", "Siddhu pednekar"))  # i can use list instead of set
    user_input = input("Enter Client Name:")

    if user_input in client_names:
        print("What u want to store:\n1.Exercise\n2.diet")
        storing_info = input("Enter Your Answer:")

        if storing_info == "1":
            exercise(user_input)
        elif storing_info == "2":
            diet(user_input)
        else:
            print("Wrong Input..")
    else:
        print("Something went wrong..")


ui()