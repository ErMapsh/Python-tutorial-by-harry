no_of_input = int(input("Enter the no of input:"))
array = [int(input("Enter the no: ")) for i in range(no_of_input)]
summ = 0
for j in array:
    addition = summ = summ + j
print(f"Addition of numbers in array: {addition}")