
from math import factorial, prod


n=4
def num(n):
    sq= n**2
    return sq
num(n)




num=int(input("enter an integer number:"))
sq=num**2
print("square root is",sq)




num = int(input("enter the number: "))
def  find_evenodd(num):
    if num % 2 ==0:
        print("even",num)
    else:
        print("odd",num)

find_evenodd(num)




num=int(input("enter the number: "))
fact=1

if num < 0:
        print("no factorial for negative no")
elif num==0:
        print("factorial of 0 is 1")
else :
        for i in range(1,num+1):
            fact=fact * i
        print("the factorial of",num,"is",fact)


 

num =10
for i in range(1,11):
    print(num ,"*", i,"=", num*i )





listA=[11,12,13,14,15]
tupA=(11,12,13,15)
setA={11,12,14,15}

print(sum(listA))
print(sum(tupA))
print(sum(setA))


print(prod(listA))
print(prod(tupA))
print(prod(setA))




string=input("enter the string")
c1=0
c2=0
for i in string:
    if (i.islower()):
        c1=c1+1
    elif (i.isupper()):
        c2=c2+1
print("the number of lower case chars is: ")
print(c1)

print("the number of upper case chars is: ")
print(c2)




def unique_list(list):
    x=[]
    for a in list:
        if a not in x:
            x.append(a)
    return x
print(unique_list([1,2,3,4,4,4,5]))


 
n=5
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i) // (factorial(j) * factorial(i-j)),end =" ")

    print( )


    #nCr =n! / (n-r)! r!
    




def isPalindrome(s):
    s=s.lower()
    l=len(s)
    if l<2:
        return True
    elif s[0] == s[l-1]:
        return isPalindrome(s[l:l-1])
    else:
        return False
s="MEEnbEEM"
ans=isPalindrome(s)
if ans:
    print("s")
else:
    print("NO")

    


def test_range(n):
    if n in range(2,9):
        print(" %s in range"%str(n))
    else:
        print("not in range")
test_range(1)







def fn(a,b):
    return a+b
print(fn(1,2))   #postion and default
print(fn(a=1,b=2)) #named



def fn(a,b,*c):
    return a,b,c
print(19,23,4,5)  #variable lenth


def team(name,id):
    print(name, "having id",id)
team(id="1",name="mee") # keyword


