# connecting database #
'''
import pymysql
mydb=pymysql.connect(host="localhost",user="root",passwd="root")
print("connected")

# creating database #
import pymysql
mydb=pymysql.connect(host="localhost",user="root",passwd="root")
print("connected")
mycursor=mydb.cursor()
mycursor.execute("create database stud")
mydb.commit()
print("database created")
mydb.close()

# creating table #
import pymysql
mydb=pymysql.connect(host="localhost",user="root",passwd="root",database="stud")
print("connected")
mycursor=mydb.cursor()
mycursor.execute("""
                create table details(stu_name varchar(20),
                stu_reg int primary key,
                stu_dept varchar(20))""")
mydb.commit()
print("table created")
mydb.close()

# inserting values #
import pymysql
mydb=pymysql.connect(host="localhost",user="root",passwd="root",database="stud")
print("connected")
mycursor=mydb.cursor()
mycursor.execute("""
                insert into details values('aaa',1001,'ece'),
                ('bbb',1002,'mech')""")
mydb.commit()
print(mycursor.rowcount,"rows inserted")
mydb.close()

# select all records #
import pymysql
mydb=pymysql.connect(host="localhost",user="root",passwd="root",database="stud")
print("connected")
mycursor=mydb.cursor()
mycursor.execute("select *from details")
myres=mycursor.fetchall()
print(type(myres))
print(myres)
print("NAME\tREGNO\tDEPARTMENT")
print("---------------------------")
for i in myres:
    print(i[0],i[1],i[2],sep="\t")
mydb.close()

# searching a record #
import pymysql
mydb=pymysql.connect(host="localhost",user="root",passwd="root",database="stud")
print("connected")
mycursor=mydb.cursor()
mycursor.execute("select *from details where stu_reg=1002")
myres=mycursor.fetchone()
print(type(myres))
print(myres)
print("NAME\tREGNO\tDEPARTMENT")
print("---------------------------")
print(myres[0],myres[1],myres[2],sep="\t")
mydb.close()

# updating values #
import pymysql
mydb=pymysql.connect(host="localhost",user="root",passwd="root",database="stud")
print("connected")
mycursor=mydb.cursor()
mycursor.execute("""update details set stu_dept='cse' where stu_reg=1001""")
mydb.commit()
print(mycursor.rowcount,"rows updated")
mydb.close()
'''
# deleting values #
import pymysql
mydb=pymysql.connect(host="localhost",user="root",passwd="root",database="stud")
print("connected")
mycursor=mydb.cursor()
mycursor.execute("""delete from details where stu_reg=1001""")
mydb.commit()
print(mycursor.rowcount,"rows deleted")
mydb.close()
