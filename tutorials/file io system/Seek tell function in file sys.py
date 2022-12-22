#in this i was use data3.txt file for accessing file

#this do for writing files

# Enter = input("Enter The String:")#already in string
# info = str(f"{Enter}\n")
# print(info)
#
# f = open('data3.txt', 'a+')
# f.write(info)
# f.close()



#in there tell pointer say index pointer
f1 = open("data3.txt", "r+")
print(f1.tell())
print(f1.readline())
print(f1.tell())
print(f1.readline())
print(f1.tell())
print(f1.readline())
print(f1.tell())

#and there is one seek pointer that reset the pointer to that index pointer
f1.seek(0)#the next thing start from that index pointer that u given in argument
print(f1.readline())
print(f1.tell())


f1.close()