class Employee:
    name=""
    eid=0
    salary=0
    def __init__(self,name,eid,salary):
        self.name=name
        self.eid=eid
        self.salary=salary
    def __str__(self):
        return self.name+"\t"+str(self.eid)+"\t"+str(self.salary)
    def find_bonus(self):
        return self.salary*0.25
    def find_pf(self):
        return self.salary*0.12

empdict={}
def add_employee(emp):
    '''
    employee={}
    employee['name']=emp.name
    employee['salary']=emp.salary
    empdict[emp.eid]=employee
    print(employee)
    '''
    empdict[emp.eid]=emp
    return "stored"
def select_employees():
    print("EMPID\tNAME\tSALARY\tBONUS\tPF")
    for i,j in empdict.items():
        print(i,end="\t")
        print(j.name,j.salary,j.find_bonus(),j.find_pf(),sep="\t")
def search_employee(eid):
    if eid in empdict.keys():
        print(empdict.get(eid))
    else:
        return "Employee Not Found"
def delete_employee(eid):
    if eid in empdict.keys():
        del empdict[eid]
        return "deleted"
    else:
        return "Employee Not Found"
def update_employee(eid,salary):
    if eid in empdict.keys():
        emp.salary=salary
        add_employee(emp)
        return "updated"
    else:
        return "Employee Not Found"
while True:
    ch=int(input("Enter The Choice:\n1.ADD\n2.SELECTALL\n3.SEARCH\n4.DELETE\n5.UPDATE"))
    if ch==1:
        name=input("Enter The Name:")
        eid=int(input("Enter The EmpID:"))
        salary=int(input("Enter The Salary:"))
        emp=Employee(name,eid,salary)
        result=add_employee(emp)
        print(result)
    elif ch==2:
        select_employees()
    elif ch==3:
        eid=int(input("Enter The EmpID:"))
        result=search_employee(eid)
        print(result)
    elif ch==4:
        eid=int(input("Enter The EmpID:"))
        result=delete_employee(eid)
        print(result)
    elif ch==5:
        eid=int(input("Enter The EmpID:"))
        salary=int(input("Enter The Salary:"))
        result=update_employee(eid,salary)
        print(result)
    else:
        break
