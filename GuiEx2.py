import tkinter as tk
from tkinter import ttk
#import mysql.connector
from tkinter.messagebox import showinfo
root=tk.Tk()
root.geometry("400x400")
root.title("Student")
'''
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",
                             database="stud")
'''
import pymysql
mydb=pymysql.connect(host="localhost",user="root",passwd="root",
                     database="stud")
mycursor=mydb.cursor()
print("connected")


namelabel=tk.Label(root,text="Student Name",bg="white",fg="blue")
namelabel.grid(row=0,column=0)
nameentry=tk.Entry(root)
nameentry.grid(row=0,column=1)

reglabel=tk.Label(root,text="Registration no",bg="white",fg="blue")
reglabel.grid(row=1,column=0)
regentry=tk.Entry(root)
regentry.grid(row=1,column=1)

deptlabel=tk.Label(root,text="Department",bg="white",fg="blue")
deptlabel.grid(row=2,column=0)
deptlist=tk.Listbox(root)
deptlist.grid(row=2,column=1)
deptlist.insert(tk.END,"Computer Science")
deptlist.insert(tk.END,"Electronics")
deptlist.insert(tk.END,"Electrical")

def save():
    mydb.ping (reconnect=True)
    sname=nameentry.get()
    sreg=int(regentry.get())
    sdept=deptlist.get(deptlist.curselection())
    mycursor.execute("insert into details values('%s',%d,'%s')"
                     %(sname,sreg,sdept))
    mydb.commit()
    showinfo("Alert", str(mycursor.rowcount)+" rows inserted")
    nameentry.delete(0, tk.END)
    regentry.delete(0, tk.END)
    deptlist.selection_clear(0)
    deptlist.selection_clear(1)
    deptlist.selection_clear(2)

def search():
    mydb.ping (reconnect=True)
    sreg=int(regentry.get())
    mycursor.execute("select *from details where stu_reg=%d"%(sreg))
    myresult=mycursor.fetchone()
    nameentry.insert(0, myresult[0])
    if myresult[2]=='Computer Science':
        deptlist.selection_set(0)
    elif myresult[2]=="Electronics":
        deptlist.selection_set(1)
    elif myresult[2]=="Electrical":
        deptlist.selection_set(2)

def update():
    mydb.ping (reconnect=True)
    sdept=deptlist.get(deptlist.curselection())
    sreg=int(regentry.get())
    mycursor.execute("update details set stu_dept='%s' where stu_reg=%d"
                     %(sdept,sreg))
    mydb.commit()
    showinfo("Alert", str(mycursor.rowcount)+" rows updated")
    nameentry.delete(0, tk.END)
    regentry.delete(0, tk.END)
    deptlist.selection_clear(0)
    deptlist.selection_clear(1)
    deptlist.selection_clear(2)

def delete():
    mydb.ping (reconnect=True)
    sreg=int(regentry.get())
    mycursor.execute("delete from details where stu_reg=%d"%(sreg))
    mydb.commit()
    showinfo("Alert", str(mycursor.rowcount)+" rows deleted")
    nameentry.delete(0, tk.END)
    regentry.delete(0, tk.END)
    deptlist.selection_clear(0)
    deptlist.selection_clear(1)
    deptlist.selection_clear(2)


def selectall():
    mydb.ping (reconnect=True)
    mycursor=mydb.cursor()
    for item in tree.get_children():
        tree.delete(item)
    mycursor.execute("select *from details")
    myres=mycursor.fetchall()
    for i in myres:
        tree.insert('',tk.END,values=i)
    
def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        nameentry.insert(0,record[0])
        showinfo(title='Information', message=record)

    
savebut=tk.Button(root,text="SAVE",command=save)
savebut.grid(row=3,column=0)
searchbut=tk.Button(root,text="SEARCH",command=search)
searchbut.grid(row=3,column=1)
updatebut=tk.Button(root,text="UPDATE",command=update)
updatebut.grid(row=4,column=0)
deletebut=tk.Button(root,text="DELETE",command=delete)
deletebut.grid(row=4,column=1)
selectbut=tk.Button(root,text="SELECT",command=selectall)
selectbut.grid(row=5,column=0)

# define columns
columns = ('student_name', 'RegisterNo', 'Department')

tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
tree.heading('student_name', text='Student Name')
tree.heading('RegisterNo', text='Regno')
tree.heading('Department', text='Department')



tree.bind('<<TreeviewSelect>>', item_selected)
#tree.pack()
tree.grid(row=6, column=0, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=6, column=1, sticky='ns')

mydb.close()
root.mainloop()
