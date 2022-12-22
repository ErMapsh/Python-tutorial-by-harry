
"""
Iterable - __iter__() or __getitem__() when we apply on object its become iterable object
Iterator - __next__() after applying iter() on object, we can access that item in object using iterator
Iteration - process of generate iterators is called iteration

"""
'''
list1 = [3, 312, 63, 345]
iterable = list1.__iter__()
print(iterable)#its begin iterable

print(iterable.__next__())#its iterator like for loop 
print(iterable.__next__())#its iterator like for loop 
print(iterable.__next__())#its iterator like for loop 
print(iterable.__next__())#its iterator like for loop 
# is similar to for loop
for i in list1:
    print(i)
'''


#Generater yeild one of the generator, we can store the data in 

def fuc(n):
    for i in range(n):
        yield  i 

data = fuc(43)
li = []
for i in data:
    li.append(i)
print(li) 

if 'ErMapsh'.__iter__():#string is iterable, then print 'yes' string is iterable
    print("'yes' stirng is iterable")