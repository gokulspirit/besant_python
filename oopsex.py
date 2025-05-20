# Object and class #
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
