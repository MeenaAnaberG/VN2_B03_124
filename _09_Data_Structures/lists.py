def sum_list(items):
    sum_numbers=0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([3,4,5,6]))



def multiply_list(items):
    multipl=1
    for x in items:
        multipl *= x
    return multipl
print(multiply_list([5,6]))



def max_num_list(list):
    max=list[0]
    for a in list:
        if a > max :
            max =a
    return max
print(max_num_list([1,2,3,4]))



def min_num_list(list):
    min=list[0]
    for a in list:
        if a < min :
            min =a
    return min
print(min_num_list([1,2,3,4]))



a=[10,20,30,20]
dup=set()
uniq=[]
for x in a:
    if x not in dup:
        
        dup.add(x)
        uniq.append(x)

print(dup)




list=[]
if not list:
    print("list is empty")



def common_data(list1,list2):
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result=True
                return result
print(common_data([1,2,3,4,5],[5,6,7,8]))



color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)



num=[2,3,4,5,6,7,8]
num=[x for x in num if x %2!=0]
print(num)


from random import shuffle 
names=['meena','nayana','maanvi','preeti']
shuffle(names)
print(names)

# list1=[2,3,4,5,6]
# list2=[1,2,3,4,5]
# diff_list1_list2=list(set(list1)-set(list2))
# diff_list2_list1=list(set(list2)-set(list1))
# total_diff=diff_list1_list2+diff_list2_list1
# print(total_diff)




