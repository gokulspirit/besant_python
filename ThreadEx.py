'''
Created on 06-Feb-2023

@author: Venkatesh

from threading import *
print("Info",current_thread())


# creating a thread using Thread Object #
from threading import *
def sub_thread():
    print("Sub Thread is running...")
def demo_thread():
    print("Demo thread is running...")

t1=Thread(target=sub_thread)
t1.start()
t2=Thread(target=demo_thread)
print("Before Start=",t2.is_alive())
t2.start()
print("After Start=",t2.is_alive())



# Creating a thread with oops #
from threading import Thread
class Mythread:
    def sub_thread(self):
        print("Sub thread is running...")

m=Mythread()
t1=Thread(target=m.sub_thread)
t1.start()


# Inheriting Thread class #
import threading
class MyThread(threading.Thread):
    def run(self)->None:
        threading.Thread.run(self)
        print("I am in run method")
m=MyThread()
m.start()
print("This is Main")


# Run the thread using sleep #
from threading import Thread
import time

def sub_thread():
    print("I am in run method",time.ctime())
    time.sleep(3)
    print("After sleep",time.ctime())

t1=Thread(target=sub_thread)
t1.start()
time.sleep(2)
print("This is main",time.ctime())


# join method #
from threading import Thread
import time

def sub_thread():
    print("I am in run method",time.ctime())
    time.sleep(5)
    print("After sleep",time.ctime())

t1=Thread(target=sub_thread)
t1.start()
time.sleep(2)
t1.join()
print("This is main",time.ctime())

'''
# Multithreading with synchronized #
import threading
import time
class MyThread(threading.Thread):
    def __init__(self,Threadid,name,delay):
        threading.Thread.__init__(self)
        self.name=name
        self.Threadid=Threadid
        self.delay=delay
    def run(self)->None:
        threading.Thread.run(self)
        print("Starting=",self.name)
        tlock.acquire()
        self.print_time(self.name,self.delay)
        tlock.release()
        print("Exited=",self.name)
    def print_time(self,name,delay):
        i=1
        while i<=5:
            time.sleep(self.delay)
            print("Thread-",self.name," ",time.ctime())
            i=i+1

tlock=threading.Lock()
m1=MyThread(1,"one",1)
m2=MyThread(2,"two",2)
m1.start()
m2.start()
m1.join()
m2.join()