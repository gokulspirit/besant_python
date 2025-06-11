# FILE IO #
'''
Streaming - produce or consume information or data.

    Data
    * Text
    * Image
    * Audio
    * Video

    Data Stored in
    * Files and Folders
    * Memory Buffer
    * Socket based Server



    Data Source - Initialize the flow of data.
    Data Destination - Terminates the flow of data.

    IO Streams

    InputStream - read the data from the source using program is called InputStream.
    OutputStream - write the data to the destination using program is called OutputStream.
------------------------------------------------------------------------------------------

    * Opening the File

    Using file object and open() method

    Ex:
        f=open(src,mode,buffer)

        src - location of the file
        mode - mode of operation ( r - read (default) , w- write , a - append)
                                   r+ - read/write w+ - write/read a+ - append/read
                                   rb - read bin, wb - write bin, ab - append bin
                                   rb+ -        wb+      ab+

        buffer - 0 (default)
        
    * Reading a File / Writing a File

        Reading a File:

            read() - read a file text as str.
            readline() - read a file text line by line.
            readlines() - read a file text as list of strings.

        Writing a File/appending a File:
            write(str) - write the str.
            writelines(list(str)) - writes the list of strings.

    * Closing a File:

        Close the file using close() method.
        
-----------------------------------------------------------------------------------------
Example:

Reading a File

f=open("E:\\IOEx\\Hello.txt","r")
#f=open("Hello.txt","r")

data=f.read()
print(type(data))
print(data)
f.close()

f=open("E:\\IOEx\\Hello.txt","r")
print(f.readline())
print(f.readline())
#print(f.readline())
f.close()

f=open("E:\\IOEx\\Hello.txt","r")
data=f.readlines()
print(data)
print(data[1])
print(type(data))
f.close()

f=open("E:\\IOEx\\Hello.txt","r")
while True:
    data=f.read(10)
    print(data)
    if not data:
        break
f.close()

-------------------------------------------------------------------------------------
Writing File

f=open("E:\\IOEx\\HelloCopy.txt","w")
f.write("Python\n")
f.write("Programming")
f.flush() # forces buffer to clear.
f.close()

f=open ("E:\\IOEx\\HelloCopy.txt","a")
#f.write ("\n also Scripting")
f.write("\n"+input("Enter The Text:"))
f.flush()
f.close()


f=open("E:\\IOEx\\HelloCopy.txt ","w")
f.writelines (["Hello\n","World"] )
f.flush()
f.close()


------------------------------------------------------------------------------------
Example for seek() - read and write text based on given position

f=open ("E:\\IOEx\\Hello.txt","r")
f.seek(8)
data=f.read()
print(data)
f.close()


f=open ("E:\\IOEx\\HelloCopy.txt","w")
f.seek(6)
f.write("Python Programming")
f.flush()
f.close()

----------------------------------------------------------------------------

File Attributes:

* name - returns the name of the file
* mode - returns the mode of operation
* closed - returns true if file is closed.otherwise false

Example:

f=open("E:\\IOEx\\HelloCopy.txt","r")
print("Name:",f.name)
print("Mode:",f.mode)
print("Before Closed:",f.closed)
f.close()
print("After Closed:",f.closed)

----------------------------------------------------------------------------------
Reading and Writing Object


import pickle
l=[100,"Hello",10.5]
f=open ("E:\\IOEx\\Objex.dat","wb")
pickle.dump(l,f)
f.flush()
f.close()


import pickle
f=open ("E:\\IOEx\\Objex.dat","rb")
l=pickle.load (f)
print(l)
f.close()

------------------------------------------------------------------------------------

import pickle
stu_list=[]
f=open("E:\\IOEx\\Student.dat","wb")
for i in range(0,3):
    student=list()
    student.append(input("Enter The Name:"))
    student.append(int(input("Enter The Regno:")))
    student.append(input("Enter The Department:"))
    stu_list.append(student)
pickle.dump(stu_list,f)
f.flush()
f.close()

import pickle
f=open("E:\\IOEx\\Student.dat","rb")
stud=pickle.load(f)
print("NAME\tREGNO\tDEPARTMENT")
print("------------------------")
for i in stud:
    print(i[0],"\t",i[1],"\t",i[2])
f.close()

--------------------------------------------------------------
'''
class Student:
    name=""
    regno=1
    def get_details(self):
        print("Name:",self.name)
        print("Regno:",self.regno)
s=Student()
s.name="aaa"
s.regno=123
#s.get_details()

import pickle
f=open("E:\\IOEx\\oops.dat","wb")
pickle.dump(s,f)
f.flush()
f.close()
    
f=open("E:\\IOEx\\oops.dat","rb")
s1=pickle.load(f)
s1.get_details()
'''
-------------------------------------------------------------
'''
