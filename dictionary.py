# in dictionary contain key value pairs

#dictionary
d1 = {}
print(type(d1))
print()

#Tuple
d2 = ()
print(type(d2))
print()

#example
d3 = {"Name": "ErMapsh", "FullName": "Mahesh Mestri", "Profession": "Engineering", "AboutFood": {"Morning": "Tea", "Launch": "Maggie", "Night": "Rice"}}
print(d3)
print(d3["FullName"])
print(d3["AboutFood"]["Morning"])
# print(d3["Name"])
# print(d3["FullName"])
print()

#small assignment
for i,j in d3.items():
    print(f'{i}:{j}')

#add something to dictionary
d3["Hobbie"] = "Programming & Gaming";
d3["Sex"] = "Male";
print("Original dictionary:",d3)

#del specific stuff form dictionary
del d3["Sex"]
print("Remove specific item form dict : ", d3)

#copy dictionary
copy_dict = d3.copy()
print("This is copy of dictionary:" , copy_dict)

#update dictionary
d3["AboutFood"].update({"Morning": "Dosa"})
print("Update specific value of key or add new key, value pair:", d3)

#dictionary keys, values, items
print(d3.keys())
print(d3.items())
print(d3.values())
