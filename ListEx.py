# Collections (Dynamic Array + Data Structures)

'''
Collection Characterstics

    * Sorted - Accessing the elements in sorting order (Unordered)
    * Ordered - Accessing the elements in insertion order (Ordered)
    * Unique - Elements Without duplicates.
    * Indexed - Accessing the elements based on index ( starts with 0)
'''

# List #
'''
* Collection of elements.
* allows different types of elements.
* mutable (object can be changed).
* ordered collection. (accessing elements based on insertion order).
* index based processing. (index starts with 0)
* allows duplicates.

creating a list (using square brackets [])

l=[] # empty list
l=[1,2,3,4]# list with similar types
l=[1,2.5,"Hello"] # list with different types
l=[1,2,[4,5],6] # list with another list
l=[[1,2],[3,4]] # 2D List
l=[1,2,3]+[4,5,6] # concatenation of list
l=list() # list with list() method
l=list([1,2,3,4])

#Accessing a List

l=[1,2.5,"hello"]
print(l)
for i in l:
    print(i)
print(l[2]) # Retrieve the particular element using index
l[1]=4.5 # changing the element using index
print(l)

del l[1] # deleting the particular element using index
print(l)
#l[2]=5
#print(l)


#Slicing: s[start:]+s[:end]

l=[12,13,10,11,15,14]
print(l[:])# It returns all the elements.[12, 13, 10, 11, 15, 14]
print(l[2:])# It returns the elements from index 2.[10, 11, 15, 14]
print(l[:4])# It returns the elements upto index 4.[12,13,10,11]
print(l[2:4])# It returns the elements from index 2 upto index 4.[10,11]
print(l[-1:])# It returns the element at index -1.(reverse) [14]
print(l[:-1])# It returns the elements upto index -1. [12,13,10,11,15]
print(l[::-1])# It returns the list in reverse.[14,15,11,10,13,12]


#Aggregate Functions

l=[1,2,3,4,5]
print("Length:",len(l))# len(iterable) - It returns the no.of elements
print("Max:",max(l))# max(iterable) - It returns the maximum element in iterable.
print("Min:",min(l))# min(iterable) - It returns the minimum element in iterable.
print("Sum:",sum(l))# sum(iterable) - It returns the total of elements in iterable.
                        #(allows numeric only)

# Note: max(),min() and sum() these methods allows only similar type of elements in iterable.

#l=[1,2.5,"Hello"]
#print(max(l)) # it returns Error

'''

#Manipulation of List using Methods

l=list()
l.append(10) # append(E) - add the given element at end of list
l.append(20)
l.append(10)
l.append(int(input("Enter The Value:")))
print("After Append:",l)
l.insert(2,15) # insert(index,E) - add the given element at specified index.
print("after insert:",l)

l1=list([30,25,35])
l.extend(l1) # extend(iterable) - add the given iterable at the end of list.
print("After extend with l1:",l)
l.insert (5,29)
print(l)
l2=l.copy() # copy() - Copies the elements of a list to another list
print("After Copy l2:",l2)

print("Index:",l.index(10))# index(E)  - It returns the first occurence of a given Element.
print("Count:",l.count(10))# count(E) - It returns no.of Occurences of a given Element.

print("Pop:",l.pop())# pop() - It returns and removes the last element of list.
print("After POP:",l)
print("Remove:",l.remove(30))# remove(E) - It removes the given element.
print("After Remove:",l)

l.reverse() # reverse() - It reverse the List.
print("After reversing:",l)
l.sort(reverse=True)# sort() - It sorting the list elements in ascending order. but list must be similar types elements
print("After Sorting:",l)

l.clear() # clear() - It removes the All elements in a list

print("After Clear:",l)
'''
---------------------------------------------------------------------------



l=[2,1,3,5,4]
temp=0
print("list before sort:",l)
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]>=l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print("list after sort:",l)
'''
