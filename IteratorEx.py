# Iterator #

'''
* Iterates all the elements of the collection.
* Using next() method.

    iter(iterable)

       iterable - Any Collection of elements.

Example:

l=[12,11,13,14,15]
for i in l:
    print(i)
  
l=[12,13,14,15,16]
my_iter=iter(l)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

my_iter=iter("banana")
print(next(my_iter))
print(next(my_iter))

#Example:
'''
class MyNumbers:
    def __iter__(self):
        self.a=10
        return self
    def __next__(self):
        self.x=self.a
        self.a=self.a+1
        return self.x
mynum=MyNumbers()
my_iter=iter(mynum)
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())



