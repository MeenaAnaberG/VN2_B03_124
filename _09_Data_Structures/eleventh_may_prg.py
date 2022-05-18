###########NESTED  LIST AS MATRIX################################

from posixpath import split


x=[[1,2,3],[4,5,6],[7,8,9]]

for i in x:
    print(i)
p=list(x[0])
q=list(x[1])
r=list(x[2])
print(p[0],p[1],p[2])
print(q[0],q[1],q[2])
print(r[0],r[1],r[2])



########sentence to list #######################
def l_words(n,str):
    word_len=[]
    txt=str.split(" ")
    for x in txt:
        if len(x) >n:
            word_len.append(x)
            
    return word_len


print(l_words(3,"meena anaber gang"))


##########tuples to list#############
def test(lst_tpl):
    result=[list(el) for el in lst_tpl]
    return result
lst_tpl=[(1,2),(6,7)]
y=[1,2,3,4]
print("original tuple")
print(lst_tpl)
print("coverted tupleto lst")
print(test(lst_tpl))

test(lst_tpl)



##sub question##
##same element
def test1(x,y):
    x_set=set(x)
    y_set=set(y)
    if (x_set == y_set):
        print(x_set & y_set)
    else:
        print("No common elements")
x=[1,2,3,4]
y=[1,2,3,4]
test1(x,y)



##########colors #######
def check_tuples(colors, c):
    result = any(c in tu for tu in colors)
    return result

colors = (
    ('Red', 'White', 'Blue'),
    ('Green', 'Pink', 'Purple'),
    ('Orange', 'Yellow', 'Lime'),
)

print("Original list:")
print(colors)

c1 = 'White'
print("\nCheck if",c1,"presenet in said tuple of tuples!")
print(check_tuples(colors, c1))

c1 = 'White'
print("\nCheck if",c1,"presenet in said tuple of tuples!")
print(check_tuples(colors, c1))

c1 = 'Olive'
print("\nCheck if",c1,"presenet in said tuple of tuples!")
print(check_tuples(colors, c1))




#################tuple of integers to single integer#########
T = (1,2,3)
print("Original List: ",T)
x = int("".join(map(str, T)))
print("Single Integer: ",x)


#############multiplication tuple#######
def mutiple_tuple(nums):
    temp = list(nums)
    product = 1 
    for x in temp:
        product *= x
    return product

nums = (4, 3, 2, 2, -1, 18)
print ("Original Tuple: ")
print(nums)
print("Product - multiplying all the numbers of the said tuple:",mutiple_tuple(nums))

nums = (2, 4, 8, 8, 3, 2, 9)
print ("\nOriginal Tuple: ")
print(nums)
print("Product - multiplying all the numbers of the said tuple:",mutiple_tuple(nums))


###########################SET#####################################

set10 = {5, 10, 3,15,25, 20}
print("Original set elements:")
print(set10)

print("\nMaximum value of the set:")
print(max(set10))
print("\nMinimum value of the set:")
print(min(set10))


#########################DICTIONARY########################


##### student data display of name,marks##
students = dict()
n = int(input("Enter number of students :"))
for i in range(n):
        sname = input("Enter names of student :")
        marks= []
        for j in range(2):
           mark = float(input("Enter marks :"))
           marks.append(mark)
        students[sname] = marks
print("Dictionary of student created :")
print(students)




#####string counting using dictionary
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('mississippi'))



#########counting of occurences of vowels in python###

vowels = 'aeiou'
ip_str = 'hi,meena here'
ip_str = ip_str.casefold()
count = {}.fromkeys(vowels,0)

for char in ip_str:
   if char in count:
       count[char] += 1

print(count)


####entering student name ,marks and enter to the dictnory##

n = int(input("Enter number of students: "))
result = {}

for i in range(n):

    print("Enter Details of student No.", i+1)
    name = input("Name: ")
    marks = int(input("Marks: "))
    result = [name, marks]
print(result)






###############OOOOOOOOOOPPPPPPSSSSSSSSSS######################

###LEAP#######
def CheckLeap(Year):
    if((Year%400 == 0 ) or (Year %100 != 0) and (Year % 4 ==0)):
        print(Year,"is Leap year")
    else:
        print(Year,"is not a Leap year")
Year=int(input("enter the number"))
CheckLeap(Year)



######ARMSTRONG##########
num=int(input("enter no: "))
sum=0
temp=num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num,"is Armstrong number")
else:
    print(num,"is not Armstrong number")



#####SIMPLE_CALCULATOR#########
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print("SElect operator")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    choice=input("enter the choice(1/2/3/4):")
    if choice in ('1','2','3','4'):
        num1=float(input("enter first number"))
        num2=float(input("enter second number"))
    if choice=='1':
        print(num1,"+",num2,'=',add(num1,num2))
    elif choice=='2':
        print(num1,"-",num2,'=',subtract(num1,num2))
    elif choice=='3':
        print(num1,"*",num2,'=',multiply(num1,num2))
    elif choice=='4':
        print(num1,"/",num2,'=',divide(num1,num2))

    nxt_cacl=input("let calculate(yes/no):")
    if nxt_cacl=="no":
        break
    else:
        print("invalid input")


#######roman to integer#########
def value(r):
    if (r=='I'):
        return 1
    if (r=='V'):
        return 5
    if (r=='X'):
        return 10
    if (r=='L'):
        return 50
    if (r=='C'):
        return 100
    if (r=='D'):
        return 500
    if (r=='E'):
        return 1000

    return -1

def romanToInteger(str):
    res=0
    i=0
    while(i<len(str)):
        s1=value(str[i])
        if(i+1  < len(str)):
            s2=value(str[i+1])
            
            if(s1>=s2):
                res=res+s1
                i=i+1
            else:
                res=res+s2-s1
                i=i+2
        else:
            res=res+s1
            i=i+1
    return res

print("integer form of roman number is: ")
print(romanToInteger("MCMIV"))
