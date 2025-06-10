 # Generator Function #
'''
* returns more than one value not using any collection object.
* return value using 'yield' keyword.

Example:

def func_1():
    return 10,20  # returning more the one value as collection

for i in func_1():
    print(i)


def func_2():
    return 10
    return 20

for i in func_2():
    print(i)
'''

def gen_func():
    yield 10
    print("Continues...")
    yield 20

    yield 30

for i in gen_func():
    print(i)

my_iter=iter(gen_func())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
    



