#its all about if, elif , else

YT_Channel = input("Enter Your YT Channel Name:");

#its all about if, elif, else
if YT_Channel == "ErMapsh":
    print("Hey Mapsh, How are you..?");
elif YT_Channel == "Shiroman":
    print("Hey Shiroman, How are you..?");
else:
    print("Who Are You MF.....ahhhh")

print()#for one blank line

#advance
list = [2, 4, 21 , 42]
if 4 in list:
    print("Yes is available in list..")



if 3 not in list:
    print("Not Available in list..")
else:
    print("Yes is available in list..")


#assignment

age = int(input("Enter Your Age:"));
if age>18:
    print("Your Are eligible for Driving..")
elif age == 18:
    print("Its Complicated to say");
else:
    print("You are not eligible for driving")