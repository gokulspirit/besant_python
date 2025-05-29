 # tuple #
'''
* Collection of elements.
* allows different types of elements.
* immutable (object cannot be changed).
* ordered collection. (accessing elements based on insertion order).
* index based processing. (index starts with 0)
* allows duplicates.

creating a tuple (using  brackets ())
t=(10,20,30)
t=tuple([Iterable])

Accessing a tuple

t=(10,20,30)
print(t)

for i in t:
    print(i)

print(t[2])

t[1]=15 # Error - tuple is immutable


print(t)
del t[1] # Error - tuple is immutable





# Slicing #
t=(12, 13, 10, 11, 15, 14)
print(t[:])# It returns all the elements.[12, 13, 10, 11, 15, 14]
print(t[2:])# It returns the elements from index 2.[10, 11, 15, 14]
print(t[:4])# It returns the elements. upto index 4.[12,13,10,11]
print(t[2:4])# It returns the elements from index 2 upto index 4.[10,11]
print(t[-1:])# It returns the element at index -1.(reverse) [14]
print(t[:-1])# It returns the elements upto index -1. [12,13,10,11,15]
print(t[::-1])# It returns the list in reverse.[14,15,11,10,13,12]


#Aggregate Functions

t=(1,2,3,4,5)
print("Length:",len(t))
print("Max:",max(t))
print("Min:",min(t))
print("Sum:",sum(t))


t=tuple("PRABHA,VELU-")
for i in t:
    print(i)

print("index:",t.index('E'))
print("count:",t.count('A'))
----------------------------------------------------------------
'''
l=[2,1,4,3,3]
print("Mean:",sum(l)//len(l))
for i in l:
    if l.count(i)>1:
        print(i)
print("method:",(max(l)-min(l)))
l.sort()
print("median:",l[len(l)//2])
