from Shape import *
print(v)
while True:
    ch=int(input("Enter The Choice:\n1.Rectangle\n2.Square\n3.Circle\n4.Exit"))
    if ch==1:
        l=int(input("Enter Length="))
        b=int(input("Enter Breadth="))
        r=rect(l,b)
        print("Area=",r)
    elif ch==2:
        a=int(input("Enter side:"))
        s=squa(a)
        print("Area=",s)
    elif ch==3:
        r=int(input("Enter radius:"))
        c=circle(r)
        print("Area=",c)
    else:
        break
print("Exited")
