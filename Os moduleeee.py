import os
# print(dir(os))

# print(os.getcwd())

'''
print(os.chdir("C://"))
print(os.getcwd())
f = open("asie hi.txt") #no such file or directoy cause of directory change 
'''
# print(os.listdir()) #all file return by this fucntion 

#Make directory fucntion 
# os.makedirs("this/that3")#ek baar file create ho jane ke baad is thorw error cause of already exit file


#Rename
# os.rename("ErMapsh.txt", "harry.txt",)#file is already renamed 

#Env
# print(os.environ.get("Path"))

#join
print(os.path.join("C://", "Er.txt"))

#exist 
print(os.path.exists("C://Er.txt"))
print(os.path.isfile("harry.txt"))
print(os.path.isdir("oops"))
