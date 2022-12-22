import pickle

#pickling data------------------
cars = ["bmw", "suzuki", "Audi", "Harryti Tuzuki", "Siddhu pednekar"]#this is a object 
file_object = open("mycar.pkl", 'wb')#this file open in write binary mode 
pickle.dump(cars, file_object) #and data store in in that file using dump
file_object.close()


#Depickling 
file_object1 = open("mycar.pkl", 'rb')#this file open in read binary mode
mycars = pickle.load(file_object1)
print(mycars)
print(type(mycars))