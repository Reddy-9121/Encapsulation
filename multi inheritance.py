MULTILEVEL INHERITANCE :- IN MULTIINHERTANCE , A CLASS INHERITS FROM A CHILD CLASS OR DERIVED CLASS .
                          SUPPOSE THREE CLASSES A , B , C IS THE SUPERCLASS ,B IS THE CHILD CLASS OF A, C IS THE CHILD CLASS OF B.

EXAMPLE:-


# Base class
class Vehicle:
    # Correct method name formatting
    def vehicle_info(self):
        print('Inside Vehicle class')

# Child class
class Car(Vehicle):
    # Correct method name formatting
    def car_info(self):
        print('Inside Car class')

# Child class of Car
class SportsCar(Car):
    # Correct method name formatting
    def sports_car_info(self):
        print('Inside SportsCar class')

# Create object of SportsCar
s_car = SportsCar()

# Access Vehicle's, Car's, and SportsCar's info using the SportsCar object
s_car.vehicle_info()    # Calls method from Vehicle
s_car.car_info()        # Calls method from Car
s_car.sports_car_info() # Calls method from SportsCar
