###############init############
class Pen:

    def __init__(self, colour, price, brand):
        self.colour = colour
        self.price = price
        self.brand = brand

    def myfunc(self):
        print("colour of pen:", self.colour)
        print("price of pen", self.price)
        print("brand of pen:", self.brand)


p1 = Pen("blue", 10, "cello")
p1.myfunc()


# Inheritance Types
# 1.single  : i super class 1 sub
# 2.multilevel : 1 super and 1 sub and 1 subsub
# 3. hierarchial : 1 super and two or more sub
# 4. hybrid  : comb of multilevel and hierarchial 
# 5. multiple : 1 sub and 2 or more sub class

#########inheirt##########
class Animal:
    def __init__(self):
        print("super class ")
    def eating(self):
        print("eating ")

class Lion(Animal):

    def __init__(self):
        print("sub class")

    def hunting(self):
        print("hunting")


leopard = Animal()  
leopard.eating()


##############without class varriable #############

class Student:
    def __init__(self, name, eid, college):
        self.name = name
        self.eid = eid
        self.college = college

    def get_studentdata(self):
        print("student information:", self.name, self.eid, self.college)


s1 = Student("Meena", "124g1a0121", "BIET")
s1.get_studentdata()

######## with class variables

class Student:

    college = "BIET"

    def __init__(self, name, sid):
        self.name = name
        self.sid = sid

    def get_studentdata(self):
        print("student details:", self.name, self.sid, Student.college)


mustafa = Student("Must", "123")
mustafa.get_studentdata()

################polymorphism###########################
a = 23
b = 11
c = 9.5
s1 = "Hello"
s2 = "world"
print(a + b)
print(type(a + b))
print(b + c)
print(type (b + c))
print(s1 + s2)
print(type(s1 + s2))



#############Method overridding###############
class Mhopping :
    def __init__(self,basket,buyer):
        self.basket=list(basket)
        self.buyer=buyer
    
    def __len__(self):
        print('Redefined length')
        count = len(self.basket)
        return count * 2

Mhopping=Mhopping(['shoes','dress'],'jessa')
print(len(Mhopping))



####### Method Overloading##############
def add(a,b,c):
    d=a+b+c
    print(d)

add(2,3,4)



#########method overriding##############
class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')



class Car(Vehicle):
    def max_speed(self):
        print('Car max speed is 240')

    def change_gear(self):
        print('Car change 7 gear')



car = Car('Car x1', 'Red', 20000)
car.show()

car.max_speed()
car.change_gear()

# Vehicle Object
vehicle = Vehicle('Truck x1', 'white', 75000)
vehicle.show()

vehicle.max_speed()
vehicle.change_gear()




#################MRO#########################
class A:
   def m1(self):
       print("m1 from A")
class B(A):
   def m1(self):
       print("m1 from B")
class C(A):
   def m1(self):
       print("m1 from C")
class D(B, C):  
   def m1(self):
       print("m1 from D")

d = D()
d.m1()
print(A.mro())
print(B.mro())  #B(A)
print(C.mro())
print(D.mro())
