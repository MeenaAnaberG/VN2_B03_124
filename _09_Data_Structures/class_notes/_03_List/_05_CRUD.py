# CRUD Operations


# 1. CREATE
list1 = [1, 2, 3, 4, 5, 6]


list1 = [1, 2, [30, 40, 50], (11, 22, 33), {1, 2, 3}, {1: 100, 2: 200}]
# 2. RETRIEVE
print('List values1 : ', list1)
print('List values2 : ', list1[2])
print('List values21 : ', list1[2][1])

# 3. UPDATE
list1[1] = 200
print('List values2 : ', list1)

# 4. DELETE
del list1[2][2]
print('List values3 : ', list1)
del list1
#print('List values4 : ', list1)


# copy - shallow copy/ deep copy


list1 = [1,2,4]
list2 = list1.copy()
print(list1, list2)

print("after append")

list1.append(100)
print(list1, list2)

print("after append list2 ")

list2.append(20)
print(list1, list2)

# we use = operator to create a copy of an object. You may think that this
# creates a new object; it doesn't.
# It only creates a new variable that shares the reference of the original object.
list1 = list2

list1.append(200)
print("after appending list1", list1, list2)
list2.append(555)
print("after appending list2",list1, list2)
'''
append 1,[1,2,3]
extend
pop
remove
count, index

dictionary methods:
items,
keys
values
has_key
from keys


'''


# shallow copy made changes to original only when you append/update nested list
# deep copy doesn't change original source

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'
print("After updating old list doesn't change newlist")
print("Old list:", old_list)
print("New list:", new_list)

new_list[1]= 'python'
print("After updating new list doesn't change original source")
print("Old list:", old_list)
print("New list:", new_list)


l1 = [1, 2,3]
l2 = copy.deepcopy(l1)

l2[1] = 100
print(l1, l2)



# shallow copy
print("performing shallow copy")
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list.append([4, 4, 4])
print("after append old_list")
print("Old list:", old_list)
print("New list:", new_list)
new_list.append(65)
print("after append new_list")
print("Old list:", old_list)
print("New list:", new_list)


# In the above program, we created a shallow copy of old_list.
# The new_list contains references to original nested objects stored in old_list.
# Then we add the new list i.e [4, 4, 4] into old_list.
# This new sublist was not copied in new_list.
#
# when you change any nested objects in old_list,
# the changes appear in new_list.

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)



l1 = [1,2,3, [1,8]]
l2 = copy.copy(l1)

l2[3][0]= 1000  # shallow copy affects original/copy soucre working o nested listed
print(l1, l2)