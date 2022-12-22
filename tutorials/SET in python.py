list_in_set = set([1, 4, 5, 43]);#set get only one agrument
print(list_in_set)
print(type(list_in_set))

#set dont allow repeat on element
s = set()
s.add(1)
s.add(1)
s.add(23)
print(s)


s1 = set([34, 46, 5])
union = s.union(s1)#all element from two or more sets, but element dosen't repeat
print("Union:", union);

s2 =  set({4, 34, 5, 23})
intersection = union.intersection(s2)
print("Intersection:", intersection)#common from two or more sets, but element dosen't repeat

#such more function in set , i was not see that, its just same as that math set