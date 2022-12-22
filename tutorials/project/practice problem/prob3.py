# ls = ['Rice Idli', 'Sambhar Vada', 'Dahi Vada', 'Dosas', 'Plain', 'Dosa (Butter)', 'Onion Dosa (Butter)', 'Paper Dosa', 'Mysore Dosa', 'Rawa Dosa', 'Onion Rawa Dosa']

ls = [3, 776, 1, 13, 32, 12]

# a= int(input("Enter no of item in list: "))
# ls = [input()for i in range(a)]


#built in function
print("using built in function:", list(reversed(ls.copy())))

#string slicing
print("string slicing:", ls.copy()[::-1])
    
#swaping last element with last one ans so on
swap_ls = ls.copy()
for i in range(len(swap_ls)):
    swap_ls[i], swap_ls[len(swap_ls) -i -1] = swap_ls[len(ls) -i -1], swap_ls[i]
    print(f"The reverese list at {i} :{swap_ls[::-1]}")
        
print(f"The reverese list : {swap_ls[::-1]}")