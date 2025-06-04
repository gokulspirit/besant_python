# Counter - returns the no.of occurences of each element as dict.#
'''
from collections import Counter

list = [1,2,3,4,1,2,6,7,3,8,1]

print(Counter(list))

cnt=Counter(list)
print("cnt[3]:",cnt[3])

---------------------------------------------------------------------------------------

from collections import defaultdict
nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
print(nums['three'])


count = defaultdict(int)
names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
for names in names_list:
    count[names] +=1
print(count)


--------------------------------------------------------------------------------

from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od[10] = 2
od['c'] = 3
print(od)

---------------------------------------------------------------------------------

from collections import deque
list = ["a","b","c"]
deq = deque(list)
print(deq)
deq.append("d")
deq.appendleft("e")
print(deq)

deq.pop()
deq.popleft()
print(deq)

--------------------------------------------------------------------------------

from collections import ChainMap
dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
print(chain_map.maps)
print(list(chain_map.keys()))
print(list(chain_map.values()))
dict3 = {'e' : 5, 'f' : 6}
new_chain_map = chain_map.new_child(dict3)
print(new_chain_map)

---------------------------------------------------------------------------------


from collections import namedtuple

Student = namedtuple('Student', 'fname, lname, age')
s1 = Student('John', 'Clarke', '13')
s2 = Student('smith', 'john', '15')
print(s1.fname)
#s1['fname']="Ricky"
print(s1)
print(s2)

----------------------------------------------------------------------------------

from collections import UserDict
ud=UserDict({'a':"apple",'b':"ball"})
print(ud.data)

ud=UserDict()
print(ud.data)

class MyDict(UserDict):
    def __del__(self):
        raise RuntimeError("not allowed")
    def pop(self, key=None):
        raise RuntimeError("not allowed")
    def popitem(self):
        raise RuntimeError("Not Allowed")
m=MyDict({'a':"apple",'b':"ball"})
print(m)
m['c']="cherry"
print(m)
m.pop('b')

-----------------------------------------------------------------

from collections import UserList
ul=UserList([1,2,3,4])
print(ul.data)

ul=UserList()
print(ul.data)

class MyList(UserList):
    def remove(self, item):
        raise RuntimeError("not allowed")
    def pop(self, i=0):
        return UserList.pop(self, i=i) #it will remove the first element
ml=MyList([1,2,3,4])
print(ml)
print(ml.pop())
print("After pop:",ml)

-----------------------------------------------------------------------


from collections import UserString

class MyString(UserString):
    def append(self, str):
        self.data=self.data+str
    def remove(self,str):
        self.data=self.data.replace(str,"")

str=MyString("This is String")
print(str)
str.append(" Hello")
print("After Append:",str)
str.remove("String")
print("After Remove:",str)

'''
