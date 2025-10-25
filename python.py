#Hierarical Inheritance
class Vehicle:
    def info(self):
        print("this is Vehicle")

class Car(Vehicle):
    def car_info(self, name):
        print("Car name is :" , name)

class Truck(Vehicle):
    def truck_info(self, name):
        print("Truck name is : " , name)

#driver code
obj1 = Car()
obj1.info()
obj1.car_info('BMW')

obj2 = Truck()
obj2.info()
obj2.truck_info('Ford')
