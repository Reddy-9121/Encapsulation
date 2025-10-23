INHERITANCE IN PYTHON

    the process of inheriting the properties of the parent class into a child class is called inheritance.
    the existing class is called a base class or parent class and the new class is called a subclass or child class or derived class.


TYPES OF INHERITANCE

in python, based upon the number of child and parent classes involved, there are five types of inheritance. the types of inheritance are listed below.

1.SINGLE INHERITANCE : in single inheritance , a child class inherits from a single-parent class. here is one child class and one parent class

   Example program:

#include <iostream>
using namespace std;

class Vehicle {
public:
    Vehicle() {
        cout << "This is a Vehicle" << endl;
    }
};

class Car : public Vehicle {
public:
    Car() {
        cout << "This Vehicle is Car" << endl;
    }
};

int main() {
   
    Car obj;
    return 0;
}

OR

# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class
class Child(Parent):
    def func2(self):
        print("This function is in child class.")

# Driver code
obj = Child()
obj.func1()
obj.func2()
                                                

2.MULTIPLE INHERITANCE : In Multiple inheritance, one class can have more than one superclass and inherit features from all parent classes.

EXAMPLE PROGRAM:

#include <iostream>
using namespace std;

class LandVehicle
{
  public:
    void landInfo()
    {
        cout << "This is a LandVehicle" << endl;
    }
};

class WaterVehicle
{
  public:
    void waterInfo()
    {
        cout << "This is a WaterVehicle" << endl;
    }
};

// Derived class inheriting from both base classes
class AmphibiousVehicle : public LandVehicle, public WaterVehicle
{
  public:
    AmphibiousVehicle()
    {
        cout << "This is an AmphibiousVehicle" << endl;
    }
};

int main()
{
    AmphibiousVehicle obj;

    obj.waterInfo();
    obj.landInfo();

    return 0;
}

OR

# Base class 1
class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)

# Base class 2
class Father:
    fathername = ""

    def father(self):
        print(self.fathername)

# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

# Driver code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()


3.MULTILEVEL INHERITANCE : Multilevel inheritance in C++ means a class is derived from another derived class, forming a chain of inheritance.

EXAMPLE PROGRAM :

#include <iostream>
using namespace std;

class Vehicle
{
  public:
    Vehicle()
    {
        cout << "This is a Vehicle" << endl;
    }
};

// Derived class from Vehicle
class FourWheeler : public Vehicle
{
  public:
    FourWheeler()
    {
        cout << "4 Wheeler Vehicles" << endl;
    }
};

// Derived class from FourWheeler
class Car : public FourWheeler
{
  public:
    Car()
    {
        cout << "This 4 Wheeler Vehicle is a Car" << endl;
    }
};

int main()
{
    Car obj;
    return 0;
}

OR

# Base class
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        # Call the constructor of Grandfather
        Grandfather.__init__(self, grandfathername)

# Derived class
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        # Call the constructor of Father
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)

# Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()


4.HIERARECHIAL INHERITANCE : In hierarchical inheritance, more than one subclass is inherited from a single base class.
                             i.e. more than one derived class is created from a single base class. For example, cars and buses both are vehicle.


EXAMPLE PROGRAM :

#include <iostream>
using namespace std;

class Vehicle
{
  public:
    Vehicle()
    {
        cout << "This is a Vehicle" << endl;
    }
};

class Car : public Vehicle
{
  public:
    Car()
    {
        cout << "This Vehicle is Car" << endl;
    }
};

class Bus : public Vehicle
{
  public:
    Bus()
    {
        cout << "This Vehicle is Bus" << endl;
    }
};

int main()
{
    Car obj1;
    Bus obj2;
    return 0;
}

OR

# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class 1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

# Derived class 2
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

# Driver code
object1 = Child1()
object2 = Child2()

object1.func1()
object1.func2()
object2.func1()
object2.func3()


5.HYBRID INHERITANCE : When two or more types of inheritance are combined in one program. For example, a class might use multiple inheritance and also be part of a multilevel inheritance chain.

EXAMPLE PROGRAM:

#include <iostream>
using namespace std;

class Vehicle
{
  public:
    Vehicle()
    {
        cout << "This is a Vehicle" << endl;
    }
};

class Fare
{
  public:
    Fare()
    {
        cout << "Fare of Vehicle" << endl;
    }
};

class Car : public Vehicle
{
  public:
    Car()
    {
        cout << "This Vehical is a Car" << endl;
    }
};

class Bus : public Vehicle, public Fare
{
  public:
    Bus()
    {
        cout << "This Vehicle is a Bus with Fare";
    }
};

int main()
{
    Bus obj2;
    return 0;
}

OR

# Base class
class School:
    def func1(self):
        print("This function is in school.")

# Derived class 1 (Single Inheritance)
class Student1(School):
    def func2(self):
        print("This function is in student 1.")

# Derived class 2 (Another Single Inheritance)
class Student2(School):
    def func3(self):
        print("This function is in student 2.")

# Derived class 3 (Multiple Inheritance)
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")

# Driver code
obj = Student3()
obj.func1()
obj.func2()
