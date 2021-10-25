mystr = "ErMapsh is good boy";
print(mystr);
print(mystr[::2]);#
print(mystr[-19::2]);#negtive string reading, but string is read by left to right always
print(mystr[::-2])#read reverse

print(mystr.isalnum())#string have white spaces that cause is not begin alphanumeric 
print("thisisfuction".isalnum())#string havent white spaces that cause return true
print(mystr.isalpha())#see all index are alphabetic
print("thisisfuction".isalpha())
print("endswith:", mystr.endswith("boy"))
print(mystr.count("o"))


print(mystr.capitalize());
print(mystr.lower())
print(mystr.upper())

print(mystr.find('good'))#find a argument in string
print(mystr.index('o'))#specify the string position
