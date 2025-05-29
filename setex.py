# Set #

'''
* Collection of elements.
* allows different types of elements.
* mutable (object can be changed).
* unordered collection.
* doesn't allows duplicates.
* doesn't allow index.

creating a set ( using {} braces)

s={}
s={1,2,3,4,5}
s=set()

#Accesing a set

s={1,2,3,3,5}
print(s)# {1,2,3,5} - doesn't allow duplicates
s={1,2,3.5,"Hello"}
print(s)# {'Hello', 1, 2, 3.5} - Unordered Collection

for i in s:
    print(i)

print(s[1]) # Error - not subscritable
#s[1]="world"

# Slicing Not Allowed #
s={1,2,3,3,5}
print(s[1:3])


Aggregate Functions

s={1,2,3,4,4,5}
print("Length:",len(s))#5 - It returns the no.of elements without duplicate
print("Max:",max(s))#5 - max(iterable) - It returns the maximum element in iterable.
print("Min:",min(s))# min(iterable) - It returns the minimum element in iterable.
print("Sum:",sum(s))# sum(iterable) - It returns the total of elements in iterable.


Manipulation Mathods
'''
s=set()
#s.add(int(input("")))
s.add(12)# add the element at end of set
s.add(13)
s.add(10)
print(s)

s1={9,15}
s.update(s1)# add the set into another set.
print(s)
print(s.discard(12))# It remove the element in set.
print("After Discard:",s)
s.remove(13)# It remove the element in set.but set is not empty
print("After remove:",s)
s={1,2,3,4}
s1={3,4,5,6}
print(s)
print(s1)
#s2=s.union{s1}
print(s.union(s1))# It combine the sets without duplicate.
print(s.intersection(s1))# It returns duplicates in both sets.
print(s.difference(s1))# It returns the unique elements from first set.
print(s.symmetric_difference(s1))


                                                                                
