# Functions #
"""
* block of statements
* execute as a unit.
* it has a behaviour.
* reduce complexity of code.
------------------------------------------------------------------------
creating a Function:

function create using 'def' keyword.
general format:

def func_name(parameters): // parameters - optional
    Statements
    return statement  // optional

Calling a Function
func_name(parameter values)#without return
var_name=func_name(parameter values)#with return

----------------------------------------------------------------------------
* without parameters and  without return

Example

def area_of_circle():
    print("After Function Call:")
    r=int(input("Enter The Radius"))#local variable
    print("Area of Circle:",(3.14*r**2))
area_of_circle()

# With parameters and without return

def peri_of_circle(r):
    print("Perimeter of Circle:",(3.14*r*2))

def area_of_circle(r):
    print("Area of Circle:",(3.14*r**2))

r=int(input("Enter The Radius:"))
area_of_circle(r)
peri_of_circle(r)

# Without parameters with return


def area_of_circle():
    r=int(input("Enter The Radius"))
    return 3.14*r**2
area=area_of_circle()
print("Area of Circle:",area)
#print("Area of Circle:",area_of_circle())


# with parameters with return

def area_of_circle(r):
    return 3.14*r**2
   
r=int(input("Enter The Radius:"))
area=area_of_circle(r)
print("Area of Circle:",area)

* return more than one value using ,

def circle_impl(r):
    return 3.14*r**2,3.14*2*r
   
r=int(input("Enter The Radius:"))
area,peri=circle_impl(r)
print("Area of Circle:",area)
print("Perimeter of circle:",peri)

------------------------------------------------------------------------------------------

# Lambda Function #

    Single Line return function
Syntax:
    lambda arguments : expression

Examples

def x(a):
    return a*5

x=lambda a:a*5
print(x(10))#50


x=lambda a,b:a if a>b else b
print("Greater :",x(10,12))#12


def func(n):
    return lambda a:a*n
x=func(10)#lambda a:a*10
print(x(5))#50


----------------------------------------------------------------------
Modules Function with same folder

Shape.py

def rect(l,b):
    return l*b
def square(a):
    return a*a
def circle(r):
    return 3.14*r**2

 ShapeImpl.py    
from Shape import * # importing all functions of Shape file
#from Shape import rect # import only rect from Shape file
#from Shape import rect,circle # importing the given function from Shape file
#from foldername.filename import * # import the module in different folder
r=rect(10,20)
s=square(10)
c=circle(12)
print("Area of Rectangle:",r)
print("Area of Square:",s)
print("Area of Circle:",c)

---------------------------------------------------------------------------------
Module Function using subfolder
from one.Shape import *
r=rect(10,20)
s=square(10)
c=circle(12)
print("Area of Rectangle:",r)
print("Area of Square:",s)
print("Area of Circle:",c)

--------------------------------------------------------------------------------
"""
# Recursive Function #
def recursion(n):
    if n==0:
        return 1
    else:
        return n*recursion(n-1)
print(recursion(6))
