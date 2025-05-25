# Object and class #
'''
class Employee:
    name=""
    eid=0
    salary=0.0
    def print_details(self):# self=obj
        print("Name=",self.name)
        print("EmpID=",self.eid)
        print("Salary=",self.salary)
    def find_bonus(self):
        return self.salary*0.25
    def find_pf(self):
        return self.salary*0.12

emp=Employee()# obj=ClassName()
while True:
    ch=int(input("Enter The Choice:\n1.ADD\n2.PRINT\n3.BONUS\n4.PF\n5.EXIT:"))
    if ch==1:
        emp.name=input("Enter The Name:")
        emp.eid=int(input("Enter The EmpID:"))
        emp.salary=float(input("Enter The Salary:"))
        print("Stored")
    elif ch==2:
        emp.print_details()
    elif ch==3:
        bonus=emp.find_bonus()
        print("Bonus=",bonus)
    elif ch==4:
        pf=emp.find_pf()
        print("Pf=",pf)
    else:
        break
print("Exited")

# Data Abstraction #
class Employee:
    name=""
    eid=0
    salary=0.0
    def print_details(self):# self=obj
        print("Name=",self.name)
        print("EmpID=",self.eid)
        print("Salary=",self.salary)
    def find_bonus(self):
        return self.salary*0.25
    def find_pf(self):
        return self.salary*0.12

emp=Employee()# obj=ClassName()
while True:
    ch=int(input("Enter The Choice:\n1.ADD\n2.PRINT\n3.BONUS\n4.PF\n5.EXIT:"))
    if ch==1:
        emp.name=input("Enter The Name:")
        emp.eid=int(input("Enter The EmpID:"))
        emp.salary=float(input("Enter The Salary:"))
        print("Stored")
    elif ch==2:
        emp.print_details()
    elif ch==3:
        if emp.salary>=20000.00:
            bonus=emp.find_bonus()
            print("Bonus=",bonus)
        else:
            print("no bonus")
    elif ch==4:
        pf=emp.find_pf()
        print("Pf=",pf)
    else:
        break
print("Exited")

# Data Encapsulation #
class Student:
    name=""
    regno=0
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def set_regno(self,regno):
        self.regno=regno
    def get_regno(self):
        return self.regno

s=Student()
name=input("Enter The Name:")
regno=int(input("Enter The Regno:"))
s.set_name(name)
s.set_regno(regno)
print("Name=",s.get_name())
print("Regno=",s.get_regno())

# Initializer #
class Employee:
    name=""
    eid=0
    salary=0.0
    def __init__(self,name,eid,salary):
        self.name=name
        self.eid=eid
        self.salary=salary
    def print_details(self):# self=obj
        print("Name=",self.name)
        print("EmpID=",self.eid)
        print("Salary=",self.salary)
    def find_bonus(self):
        return self.salary*0.25
    def find_pf(self):
        return self.salary*0.12

#emp=Employee()# obj=ClassName()
while True:
    ch=int(input("Enter The Choice:\n1.ADD\n2.PRINT\n3.BONUS\n4.PF\n5.EXIT:"))
    if ch==1:
        name=input("Enter The Name:")
        eid=int(input("Enter The EmpID:"))
        salary=float(input("Enter The Salary:"))
        emp=Employee(name,eid,salary)
        print("Stored")
    elif ch==2:
        emp.print_details()
    elif ch==3:
        bonus=emp.find_bonus()
        print("Bonus=",bonus)
    elif ch==4:
        pf=emp.find_pf()
        print("Pf=",pf)
    else:
        break
print("Exited")


# non-self #
class Arith:
    a,b=0,0
    def print_details():
        print("a=",Arith.a)
        print("b=",Arith.b)
    def add(self):
        return Arith.a+Arith.b

ar=Arith()
Arith.a=10
Arith.b=20
Arith.print_details()
print(ar.add())

# Inheritance #
# Single Inheritance #
class Employee:
    name=""
    eid=0
    salary=0.0
    def set_details(self,name,eid,salary):
        self.name=name
        self.eid=eid
        self.salary=salary
    def print_details(self):# self=obj
        print("Name=",self.name)
        print("EmpID=",self.eid)
        print("Salary=",self.salary)
        
class Bonus(Employee):
    def find_bonus(self):
        return self.salary*0.25
    def find_pf(self):
        return self.salary*0.12

emp=Bonus()
while True:
    ch=int(input("Enter The Choice:\n1.ADD\n2.PRINT\n3.BONUS\n4.PF\n5.EXIT:"))
    if ch==1:
        name=input("Enter The Name:")
        eid=int(input("Enter The EmpID:"))
        salary=float(input("Enter The Salary:"))
        emp.set_details(name,eid,salary)
        print("Stored")
    elif ch==2:
        emp.print_details()
    elif ch==3:
        bonus=emp.find_bonus()
        print("Bonus=",bonus)
    elif ch==4:
        pf=emp.find_pf()
        print("Pf=",pf)
    else:
        break
print("Exited")

# Multilevel Inheritance #
class Employee:
    name=""
    eid=0
    salary=0.0
    def set_details(self,name,eid,salary):
        self.name=name
        self.eid=eid
        self.salary=salary
    def print_details(self):# self=obj
        print("Name=",self.name)
        print("EmpID=",self.eid)
        print("Salary=",self.salary)

class Pf(Employee):
    def find_pf(self):
        return self.salary*0.12
    
class Bonus(Pf):
    def find_bonus(self):
        return self.salary*0.25
    
emp=Bonus()
while True:
    ch=int(input("Enter The Choice:\n1.ADD\n2.PRINT\n3.BONUS\n4.PF\n5.EXIT:"))
    if ch==1:
        name=input("Enter The Name:")
        eid=int(input("Enter The EmpID:"))
        salary=float(input("Enter The Salary:"))
        emp.set_details(name,eid,salary)
        print("Stored")
    elif ch==2:
        emp.print_details()
    elif ch==3:
        bonus=emp.find_bonus()
        print("Bonus=",bonus)
    elif ch==4:
        pf=emp.find_pf()
        print("Pf=",pf)
    else:
        break
print("Exited")

# Multiple Inheritance #
class Employee:
    name=""
    eid=0
    salary=0.0
    def set_details(self,name,eid,salary):
        self.name=name
        self.eid=eid
        self.salary=salary
    def print_details(self):# self=obj
        print("Name=",self.name)
        print("EmpID=",self.eid)
        print("Salary=",self.salary)

class Pf:
    def find_pf(self):
        return self.salary*0.12
    
class Bonus(Pf,Employee):
    def find_bonus(self):
        return self.salary*0.25
    
emp=Bonus()
while True:
    ch=int(input("Enter The Choice:\n1.ADD\n2.PRINT\n3.BONUS\n4.PF\n5.EXIT:"))
    if ch==1:
        name=input("Enter The Name:")
        eid=int(input("Enter The EmpID:"))
        salary=float(input("Enter The Salary:"))
        emp.set_details(name,eid,salary)
        print("Stored")
    elif ch==2:
        emp.print_details()
    elif ch==3:
        bonus=emp.find_bonus()
        print("Bonus=",bonus)
    elif ch==4:
        pf=emp.find_pf()
        print("Pf=",pf)
    else:
        break
print("Exited")

# Hierarchical Inheritance #
class Employee:
    name=""
    eid=0
    salary=0.0
    def set_details(self,name,eid,salary):
        self.name=name
        self.eid=eid
        self.salary=salary
    def print_details(self):# self=obj
        print("Name=",self.name)
        print("EmpID=",self.eid)
        print("Salary=",self.salary)

class Pf(Employee):
    def find_pf(self):
        return self.salary*0.12
    
class Bonus(Employee):
    def find_bonus(self):
        return self.salary*0.25
    
emp=Bonus()
epf=Pf()
while True:
    ch=int(input("Enter The Choice:\n1.ADD\n2.PRINT\n3.BONUS\n4.PF\n5.EXIT:"))
    if ch==1:
        name=input("Enter The Name:")
        eid=int(input("Enter The EmpID:"))
        salary=float(input("Enter The Salary:"))
        emp.set_details(name,eid,salary)
        epf.set_details(name,eid,salary)
        print("Stored")
    elif ch==2:
        emp.print_details()
    elif ch==3:
        bonus=emp.find_bonus()
        print("Bonus=",bonus)
    elif ch==4:
        pf=epf.find_pf()
        print("Pf=",pf)
    else:
        break
print("Exited")

# Polymorphism #
# compile time - Method Overloading #
class Shape:
    def area(self,a=None,b=None):
        if a!=None and b!=None:
            print("Rectangle=",(a*b))
        elif a!=None:
            print("Square=",(a*a))
        else:
            print("no area")


s=Shape()
s.area()
s.area(10)
s.area(10,20)

# Runtime - MethodOverriding #
class Area:
    def circle(self,r):
        print("Area=",(3.14*r**2))
class Perimeter(Area):
    def circle(self,r):
        print("Perimeter=",(3.14*2*r))
        super().circle(r)

p=Perimeter()
p.circle(10)

# Abstract class #
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Barking")

d=Dog()
d.sound()
'''
