

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