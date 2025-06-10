#Higher Order functions #
# map(function,iterable)
s="12345"
m=list(map(int,s))
print(m)

n=list(map(lambda a:a*5,m))
print(n)

# filter(function,iterable)
n=list(filter(lambda a:a%2==0,m))
print(n)

# reduce(function,iterable)
from functools import reduce
n=reduce(lambda a,b:(a+b),m)
print(n)
