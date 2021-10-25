list = [["Harry", 3], ["Larry", 4], ["Karry", 6]];

dict = dict(list)
print(dict)

for item, value in dict.items():
    print(item,"and lolly value is", value)


random_list = [34, 4, 53, 43, 2, 5 , 'int', 3, 32]
for item in random_list:
    if str(item).isnumeric():
        print(item)
    else:
        print("expect isnumeric items:", item)

