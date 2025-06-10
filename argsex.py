'''
def func(*argv):
    for i in argv:
        print(i)
func("Hello","World","welcome")

def func1(arg1,*argv):
    print(arg1)
func1("Hello","World","welcome")

def func2(**kwargs):
    for i,j in kwargs.items():
        print(i,"=",j)
func2(a="apple",b="banana")

def func3(a,**kwargs):
    print(a)
func3(a="apple",b="banana")
'''
class test:
    def __init__(self):
        self.variable = 'Old'
        self.Change(self.variable)
    def Change(self, var):
        var = 'New'
obj=test()
print(obj.variable)




