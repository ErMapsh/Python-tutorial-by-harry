lis = ['a', 'b', 'c', 'd']

# i = 1
# for item in lis:
#     if i % 2 != 0:
#         print(f"jarvis by this:{item}")
#     i += 1

# In short: this function give u index, item at a time
for index, item in enumerate(lis): 
    if index%2 == 0:
        print(f"jarvis by this:{item}")

