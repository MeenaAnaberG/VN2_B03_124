nestedList = [1,2,3,4,[5,6,7,8]]
subList = nestedList[4]
try:
    print(subList)
except:
    print("list doesnt support nested list") 



list={"a":"meena","b":"preeti","c":"harsha"}
print(type(list))




X=[1,2,3]
Y=[5,6,7]
sum=[a+b for a,b in zip(X,Y)]
print(sum)




i=0
StuName=None
ID=None
students={}
while 1:
    i+=1
    student=input('enter student name and ID or q to exit')
    if student=='q':
        break
    else:
        StuName,ID = student.split(',')
        students.update({StuName:ID})

for StuName,ID in students.items():
    print('Name:{} \t ID:{}'.format(StuName,ID))



my_list={10:150,20:100,25:250,34:250}

print("initial dict",str(my_list))

rev_dict={ }

for key,value in my_list.items():
    rev_dict.setdefault(value,set()).add(key)
    
result=[key for key,values in rev_dict.items() if len(values)>1]
print("duplicate values",str(result)) 













