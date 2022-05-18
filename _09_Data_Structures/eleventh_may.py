#######################################LIST#################################################################

#TRAVERSING of element  in list


#WHILE
list=[7,7,8,9]
length=len(list)
print(len(list))

i=0
while i < length:
    print(list[i])
    i+=1



#FOR
list=[7,7,8,9]

for i in list:
    print(i)




#display even numbers
list=[7,7,8,9]

for num in list:
    if num%2==0:
        print(num,"even number")
   



#display elements by index wises
list=[-7,7,8,9]
for num in list:
    if num<0:
        print(num)
    # elif num>0:
    #     print(num)
    





###########impt functions of list################

##len,count,index##
list=[-7,7,8,9]
def lst(list):
    print(len(list))
lst(list)


txt="meena anaber gang meena"
substring="meena"
def text(txt):
    occ=txt.count(substring)
    print("there are",str(occ),"occurence of",substring)
text(txt)



list=[-7,7,8,9]
def lst(list):
    for num in list:
        if num<0:
            print(num)

lst(list)





##manipulating elements of list##

##append() it adds to cuurent not creating new list
list=[-7,7,8,9]
def lst(list):
    list.append(1)
    print(list)

lst(list)


##insert() it adds the element @specified position
list=[-7,7,8,9]
def lst(list):
    list.insert(1,"1")
    print(list)

lst(list)




##difference odd append and insert##
##append() it adds to cuurent not creating new list

##insert() it adds the element @specified position
list=[-7,7,8,9]
def lst(list):
    list.append(1)
    list.insert(1,"1")
    print(list)

lst(list)


##extend() add iterable element at the end of the list 
## we add tuples,sets in list @end of list

##list,tuple
list=[-7,7,8,9]
tuple=(-7,7,8,9)


def lst(list):
    list.extend(tuple)
    print(list)

lst(list)


##list,set
list=[-7,7,8,9]
set={-7,7,8,9}

def lst(list):                          
    list.extend(set)
    print(list)

lst(list)


##remove() use to delete the data from list 
list=[-7,7,8,9]
def lst(list):
    list.remove(7)
    print(list)

lst(list)



##pop() use to delete the data from list using the index value and return the popped up data
list=[-7,7,8,9]
def lst(list):
    list.pop(2)
    print(list)

lst(list)




##difference between remove and pop is deletes data and but these 2 are builtin ()

##remove() use to delete the data from list 
##pop() use to delete the data from list using the index value and return the popped up data
list=[-7,7,8,9]
def lst(list):
    list.remove(7)
    list.pop(1)
    print(list)

lst(list)



##ordering elements##

##reverse() reverse of elements in list
list=[-7,7,8,9]
def lst(list):
    list.reverse()
    print(list)

lst(list)


##sort() it will be ascending by default ,but it sorted in reverse too
list=[4,5,0,-4,-7,7,8,9]
def lst(list):
    print(list)
    list.sort()
    print(list)

lst(list)



#############################ALIASING  and CLONING ###########################################
##SLICE() =  return object

list=[-7,7,8,9]
def lst(list):
    print(list[0:-2])

lst(list)


##copy() =returns new list 
list=[-7,7,8,9]
def lst(list):
    print(list)
    nm=list.copy()
    print(nm)

lst(list)







############################################TUPLE########################################################################
###accessing elements#######

##by using index
tuple1=('m','e','e','n','a')
print(tuple1[3])

##by using slice
tuple2=('m','e','e','n','a')
print(tuple2[1:3])

##  +  and * 
print((1,2,3)+(1,2,3))

print(("nee",)*4)


####imortant functions of tuple##########
##Length of tuple
aa=('a','n','m')
print(len(aa))


##count of tuple
aa=(1,2,3,4,1)
print(aa.count(2))


##index of tuple
aa=('a','n','m','p','e','a')
vowels=aa.index('e')
print("index of vowel: ",vowels)


##sorted
aa=(1,2,3,4,1)
result=sorted(aa)
print("sorted tuple: ",result)


##min
aa=(1,2,3,4,1)
result=min(aa)
print("min tuple: ",result)


##max
aa=(1,2,3,4,1)
result=max(aa)
print("max tuple: ",result)


##unpacking of tuple uses * ##

## unpacking -assigning a tuple into multiple variables 
def rs(x,y):
    return x*y
print(rs(10,10))
z=(10,10)

print(rs(*z))

## packing- assigning multiple values to tuple
s1=(1,"meena",2012,"aaa")
print(s1)




