'''
ls = []

for i in range(100):
    if i%3 == 0:
        ls.append(i)
print(ls)
'''

#list compression
ls = [i for i in range(100) if i%3 == 0]
# print(ls)


#dictiornary comprehsion
dc = { i:f"Item{i}" for i in range(10) if i%2 == 0}
dc1 = {value:key for key, value in dc.items()}
# print(dc, "\n", dc1)

#set comprehsion : 
dress = {dress for dress in ["dress1", "dress3", "dress1", "dress1", "dress3" , "dress2"]}
# print(dress)
# print(type(dress))


#generator compreshsion

even = (i for i in range(1, 101) if i%2 == 0) #yeild ke bajay , round bracket/ parenthesis using for generator
# print(type(even))

#=========================Excersice ------------------
def ans(NI, toc):
    if toc == "1":
        lis = [input(f"Enter the thing no {i}: ") for i in range(1, NI+1)]
        print(lis)
    elif toc == "2":
        dic = {f"item{i}": {input(f"Enter the thing no {i}: ")}  for i in range(1, NI+1) }
        print(dic)

    elif toc == "3":
        sets = {input(f"Enter the thing no {i}: ") for i in range(1, NI+1)}
        print(sets)

    else:
        print("Something Wrong")

        

noInput = int(input("How may thing that u wana store:"))
print("1.List\n2.Dictionary\n3.Set")
typeOfComprehsion = input("which type of Compreshsion do u want(ans in digit like 2 for Dictionary :")

ans(noInput, typeOfComprehsion)