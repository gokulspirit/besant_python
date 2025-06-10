# Exception Handling #
'''
What is Exception?
    * An Interrupt occurs during execution of the program.
    * It occurs and terminate the normal flow of program.
    Interrupt - User Input , Resource problem

Keywords:

    * try - It will monitors the exception code.
         - once exception occurs it will terminate the code immediately.
         - call except or finally block.

    * except - It will handle exception based on type
             - sends the message

    * finally - Always executed. used for closing resources.
              - Otherwise use some print statements.

General Format:

    try:
        monitors the exception code
        //statements
    except exceptionclasstype:
        //statements
    except ...

    finally:
        //statements

Example:
Without Exception Handling

a,b = 10,0
c=a/b
print(c)
print("welcome")

#With Exception Handling
a,b = 10,0
try:
    c=a/b
    print(c)
except ZeroDivisionError: #Exception
    print("Don\'t use b as zero")
finally:
    print("always executed")
print("welcome")

'''
#Multiple Exception Handling

try:
    a=int(input("Enter a="))
    b=int(input("Enter b="))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Don\'t use b as zero")
except ValueError:
    print("use only digits[0-9]")
except Exception:
    print("others")


#try with else

try:
    a=int(input("Enter a="))
    b=int(input("Enter b="))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Don\'t use b as zero")
except ValueError:
    print("use only digits")
except Exception:
    print("others")
else:
    print("no Error")  # else will execute when try not have any exception.


    * raise - used to call explicit exception.
            - also used to call custom exception

Example for raise            

def validate(age):
    if age<18:
        #print("not eligible for voting")
        raise RuntimeError("not eligible for voting")
    else:
        print("welcome")
validate(17)
print("rest of code...")

#Example for Custom Exception

class MyException(Exception): # creating custom exception named MyException using Exception class
    def __init__(self,msg):
        self.msg=msg
        print(self.msg)

def validate(age):
    if age<18:
        raise MyException("not eligible for voting") # call custom exception named MyException
    else:
        print("welcome")
validate(17)
print("rest of code...")


'''
