  
# Dictionary #
'''

* Collection of Elements.
* Accessing the Elements based on Key-Value Pair.
* Key must be unique.
* Unordered Collection.
* mutable. (Object can be changed)
* Key based processing.

Creating a Dictionary ( using {} braces)
d={}
d={'a':"apple",'b':2}
d=dict()


Accessing a Dictionary

d={'a':"apple",'b':2}
print(d)
d['c']=10.5
print(d)# It returns all the elements in Key-value pair
print(d['a'])# It returns the value of the particular Key.
del d['b'] # It removes the given key-value pair.
print(d)
print(len(d)) # It returns the no.of pairs.

#Manipulation Mathods

'''
d=dict()
d['a']="apple" # adding the element at end of dict.
d[10]="android"
d['c']="Cherry"
print(d)
d1={'e':"element"}
d.update(d1)# adding the dict at end of dict.
print(d)
print(d.items())# it returns the Key-Value pair in list of tuples.
for i,j in d.items():
    print(i," ",j)
print(d.keys())# It returns the Keys only.
print(d.values())# It returns the value only.
print(d.popitem())# It removes the last element.
print("After Popitem:",d)
print(d.pop('a'))# It removes the given key.
print("after pop:",d)
print(d.get('c'))# It returns the value of given key
d.clear()
print("After Clear:",d)


