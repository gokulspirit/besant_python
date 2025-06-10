def Hello(s):
    return s.upper()
print(Hello("This is Decorator"))

world=Hello
print(world("This is Decorator"))


def greet(func):
    print(func("This is decor with arguments"))

greet(Hello)
greet(world)


def create_add(x):
    def add(y): 
        print("y=",y)
        return x+y
    return add
z=create_add(10)#add
#print(z)
print(z(20))#add(20)


