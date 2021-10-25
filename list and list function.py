list1 = ["i", "am", "Mahesh Mestri"];

# for i in list1:
#     print(i, end=" ");

numbers = [4, 34, 1, 8, 7, 46, 6, 8, 0,4, 4];
# numbers.sort();
# numbers.reverse();

# slicing
print(numbers[::-1]);#return reverse string and read by left to right
print("length of string:", len(numbers))
print(numbers[-1::-2]);
print(numbers[-1:-6:-1]);#we use -1 so print from backward
print(min(numbers))
print(max(numbers))

#small assignment
new_list = []
try:
    for i in range(0, 5):
        no = int(input("Enter no: "));
        new_list.append(no);

except Exception as e:
    print(e);

#list sorting using sort function
new_list.sort();
print("new list there using user input no:", new_list);

#list clear using clear function
new_list.clear();
print('using clear() function on list:',new_list);

#copy list unsing copy function
numbers_copy = numbers.copy();
print('copy list unsing copy function:',numbers_copy);

#count specific item in list
print('count specific item in list:', numbers_copy.count(4));

# adds iterable elements to the end of the list
exp_list = [1, 4, 4, 5];
exp_list.extend([56, 34, 23])
print(exp_list);

# returns the index of the element in the list
print('returns the index of the element in the list:', exp_list.index(5))


# insert an element to the list #insert the element on that index no
exp2 = [3, 5, 32, 45, 4]
exp2.insert(4, 433)
print(exp2)

# Removes element at the given index
exp2.pop(2)
print(exp2)

