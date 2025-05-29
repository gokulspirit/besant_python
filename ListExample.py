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

emplist=[]
def add_employee(emp):
    if len(emplist)>0:
        for i in range(len(emplist)):
            if emplist[i].eid==emp.eid:
                return "Already exists"
            else:
                emplist.append(emp)
                return "stored"
    else:
        emplist.append(emp)
        return "stored"
def select_employees():
    print("NAME\tEMPID\tSALARY\tBONUS\tPF")
    for i in emplist:
        print(i,i.find_bonus(),i.find_pf(),sep="\t")
def search_employee(eid):
    flag=False
    for i in range(len(emplist)):
        if emplist[i].eid==eid:
            flag=True
            
    if flag==True:
        for i in range(len(emplist)):
            if emplist[i].eid==eid:
                return emplist[i]
    else:
        return "Employee Not Found"
def delete_employee(eid):
    flag=False
    for i in range(len(emplist)):
        if emplist[i].eid==eid:
            flag=True
            
    if flag==True:
        for i in range(len(emplist)):
            if emplist[i].eid==eid:
                del emplist[i]
                return "deleted"
    else:
        return "Employee Not Found"
def update_employee(eid,salary):
    flag=False
    for i in range(len(emplist)):
        if emplist[i].eid==eid:
            flag=True
            
    if flag==True:
        for i in range(len(emplist)):
            if emplist[i].eid==eid:
                emplist[i].salary=salary
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
        
        
