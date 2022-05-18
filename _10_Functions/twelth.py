########append()
def fast (items= []):
    items.append (1)
    return items

print (fast ())
print (fast ())

###print string for given length
keyword = 'misallenous'
print (keyword [:2] + keyword [4:])




#########find duplicate letters 
duplicates = ['a','b','c','d','d','d','e','a','b','f','g','g','h']

uniqueItems = list(set(duplicates))
print (sorted(uniqueItems))



########match the word which is having same character within same string
def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221','xpq']))




##### removing 0,4,5th element
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)



##### printing the square of each except from 1 to 5 till 30
def printValues():
	l = list()
	for i in range(1,31):
		l.append(i**2)
	print(l[5:])

printValues()



####list into string
L = [11, 33, 50]
print("Original List: ",L)
x = int("".join(map(str, L)))
print("Single Integer: ",x)





#### replace n with n+1 value

# def change_pos(my_list):
#     for i in range(0,len(my_list),2):
#         my_list[i],my_list[i+1]= my_list[i+1],my_list[i]
#         return my_list
# my_list=[0,1,2,3,4,5]
# print(change_pos(my_list))





from itertools import zip_longest, chain, tee
def replace2copy(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
n = [0,1,2,3,4,5]
print(replace2copy(n))



#### string reverse
def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))



##### counting upper and lower case
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')



class Test():
    def __init__(self):
        self.x = 1
 
t = Test()
print (t.x)







