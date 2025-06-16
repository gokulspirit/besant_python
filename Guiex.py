# GUI - Graphical User Interface #
# creating window #
'''
from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
#root.configure(bg="red")
root.configure(bg="#FF00FF")# RGB (00-FF)(0-9,A-F)
root.mainloop()

# creating frame #
from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
root.configure(bg="#FF00FF")
f=Frame(root,width=200,height=200,bg="red")
f.pack()
f1=Frame(root,width=200,height=200,bg="green")
f1.pack(side="left")
root.mainloop()


Layouts

packer - pack()

side="top"(default),"left","right","bottom"
padx=int,pady=int
anchor='n','e','w','s','ne','nw','se','sw'

grid - grid(row=int,column=int)

# UI Widgets - Label #
from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
root.configure(bg="#FF00FF")
l=Label(root,text="Hello World",bg="red",fg="white",font={'Arial',20})
l.pack()
root.mainloop()

# UI Widgets - Button #
from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
root.configure(bg="#FF00FF")
def button_clicked():
    print("button clicked")
b=Button(root,text="Click",command=button_clicked)
b.pack()
root.mainloop()

# UI Widgets - Dynamic Label #
from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
root.configure(bg="#FF00FF")
v=StringVar()
l=Label(root,textvariable=v,bg="red",fg="white",font={'Arial',20})
l.pack()
v.set("Hello World")
def set_label():
    v.set("Welcome to Besant")
def get_label():
    print(v.get())
b=Button(root,text="Click",command=set_label)
b.pack()
b1=Button(root,text="Get",command=get_label)
b1.pack()
root.mainloop()

# UI Widgets - Entry #
from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
root.configure(bg="#FF00FF")
v=StringVar()
l=Label(root,textvariable=v,bg="red",fg="white",font={'Arial',20})
l.pack()
v.set("Hello World")
e=Entry(root)
e.pack()
e.insert(0,"Hello")
def set_label():
    v.set("Welcome:"+e.get())
b=Button(root,text="Click",command=set_label)
b.pack()
root.mainloop()

# UI Widgets - Text #
from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
root.configure(bg="#FF00FF")
t=Text(root,width=25,height=5)
t.pack()
def write_data():
    f=open("guitext.txt","w")
    f.write(t.get(0.0,END))
    f.flush()
    f.close()
    t.delete(0.0,END)
def read_data():
    t.delete(0.0,END)
    f=open("guitext.txt","r")
    data=f.read()
    t.insert(0.0,data)
    f.close()
b1=Button(root,text="Write",command=write_data)
b1.pack()
b2=Button(root,text="Read",command=read_data)
b2.pack()
root.mainloop()

# UI Widgets - Listbox #
from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
root.configure(bg="#FF00FF")
l=Listbox(root)
l.pack()
l.insert(END,"cse")
for i in ["ece","eee","mech"]:
    l.insert(END,i)
e=Entry(root)
e.pack()

def select():
    e.delete(0,END)
    e.insert(0,l.get(l.curselection()))
b=Button(root,text="Click",command=select)
b.pack()
root.mainloop()

# UI Widgets - Combobox #
import tkinter as tk
from tkinter import ttk,StringVar
root=tk.Tk()
root.geometry("400x400")
root.title("My Window")
root.configure(bg="#FF00FF")
v=StringVar()
day=ttk.Combobox(root,textvariable=v)
day['values']=('sun','mon','tue','wed','thu','fri','sat')
day.pack()
day.current(3)
e=ttk.Entry(root)
e.pack()
def select():
    e.delete(0,tk.END)
    e.insert(0,v.get())
b=ttk.Button(root,text="Click",command=select)
b.pack()
root.mainloop()

# UI Widgets - Checkbutton #
from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
root.configure(bg="#FF00FF")
c1=IntVar()
c2=IntVar()
e=Entry(root)
e.pack()
def choose():
    if c1.get()==1:
        e.delete(0,END)
        e.insert(0,"B.E")
    if c2.get()==1:
        e.delete(0,END)
        e.insert(0,"M.E")
cb1=Checkbutton(root,text="U.G",command=choose,variable=c1)
cb1.pack()
cb2=Checkbutton(root,text="P.G",command=choose,variable=c2)
cb2.pack()
root.mainloop()

# UI Widgets - Radiobutton #
from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
root.configure(bg="#FF00FF")
v=StringVar()
e=Entry(root)
e.pack()
def choose():
    e.delete(0,END)
    e.insert(0,v.get())
rb1=Radiobutton(root,text="Male",value="male",command=choose,variable=v)
rb1.pack()
rb2=Radiobutton(root,text="Female",value="female",command=choose,variable=v)
rb2.pack()
root.mainloop()
'''
# UI Widgets - Checkbutton #
from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
menubar=Menu(root)
def newmenu():
    e.delete(0,END)
    e.insert(0,"New File")
    
filemenu=Menu(menubar)
filemenu.add_command(label="New",command=newmenu)
filemenu.add_separator()
menubar.add_cascade(label="File",menu=filemenu)

submenu=Menu(filemenu)
submenu.add_command(label="Exit",command=root.destroy)
filemenu.add_cascade(label="Close",menu=submenu)

e=Entry(root)
e.pack()
    
root.configure(bg="#FF00FF",menu=menubar)
root.mainloop()
