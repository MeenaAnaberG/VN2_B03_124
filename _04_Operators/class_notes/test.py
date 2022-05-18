x = -10
y = 4



print(x + y)
print(x - y)
print(x * y)
print(x/y)
print(x % y)
print(x ** y)
print(x // y)

print("Relational operator")
x = 100
y = 110


print(x == y)  # comparing values
print(x != y)   # Not equals
print(x > y)   #Greater than
print(x < y)  # lesser than
print(x >= y) # Greater than or equals to
print(x <= y)  # Lesser than or equals to

# Assignment operators

x = 10  # assign operator
y = 20

#res = x+y  # +=
print(x+y)


y = 10
print(id(x), id(y))


x = int(input("Enter first number:"))
y = int(input("Enter second number:"))

result = x + y

print("End output:", result)


print(x==y)  # comparing values
print(x is not y) # comparing memory locations

x = [10, 11, 20, 15]

print(10 in x)
print(22 not in x)