# String #
'''
* Collection of characters
* immutable. (Object doesn't change)
* enclosed with single quote('') or double quote(" ")
* ordered collection.
* index based processing.

creation of string

s="Hello"

Accessing of Characters



s="Hello"
print(s[2])# it returns the character at specified index.

for i in s:
    print(i)

#s[2]='e' # Error - immutable
#print(s)
#del s[2] # Error - 'str' object doesn't support item deletion

Slicing

s="welcome"
print(s[:])# welcome - It returns all the characters.
print(s[2:])# lcome - It returns characters from index 2.
print(s[:2])# we - It returns characters upto index 2.
print(s[3:7])# come - It returns characters from 3 to 7.
print(s[-1:]) # e - It returns the last character.
print(s[:-1])# welcom - It returns the characters before -1.
print(s[::-1])# emoclew - It returns the string in reverse.

Aggregate Functions

s="welcome"
print("Length:",len(s))# 7
print("Max:",max(s))# w   ( max(),min()-based on Ascii value A-Z=65-90 a-z=97-122 0-9=48-57)
print("Min:",min(s))# c
#print("Sum:",sum(s))#error

print("Concatenation:",('Hello'+' world'))# Hello world
print("Replication:",("Hi"*5))#HiHiHiHiHi


String Methods
'''
s="welcome"
print(s)
s="hello world"
print("Before:",s)# hello world
print("Capitalize:",s.capitalize())# Hello world - It returns the first letter in uppercase.
print("After:",s)# hello world

print("Title:",s.title())# Hello World - It returns the all the words of string first letter in uppercase.

print("Center:",s.center(15,'*'))# **hello world**
print("Ljust:",s.ljust(15,'*'))# hello world****
print("Rjust:",s.rjust(15,'*'))# ****hello world

print("Count:",s.count('l',0,len(s)))# 3 - It returns the no.of occurences of a given str.
print("Count:",s.count('l',0,5))# 2

print("Find:",s.find('l',0,len(s)))# 2 - It returns the first occurence of given str.
print("rfind:",s.rfind('l',0,len(s)))# 9 - It returns the last occurence of given str.
print("Find:",s.find('a',0,len(s))) # -1 - returns if the given str is not available.

print("Index:",s.index('l',0,len(s)))# 2 - It returns the first occurence of given str.
print("rindex:",s.rindex('l',0,len(s)))# 9 - It returns the last occurence of given str.
#print("index:",s.index('a',0,len(s))) #  returns ValueError: substring not found.


s="Hello World"
print("replace:",s.replace('Hello','welcome'))#welcome world - It replaces the given original str into replaced str
print("lowercase:",s.lower())# hello world - Convert all the characters into lowercase.
print("uppercase:",s.upper())# HELLO WORLD - Convert all the characters into uppercase.
print("Swapcase:",s.swapcase())# hELLO wORLD - swaping the charcters from upper to lower and vice versa.
print("partition:",s.partition("o"))# ('Hell', 'o', ' World')

s1=s.split("o")# ['Hell', ' W', 'rld'] - It converts str into list of str using delimiter.
print(s1)


s="a"
print("alpha:",s.isalpha()) # True - when the character is alphabet. Otherwise False
print("isalnum:",s.isalnum()) # True - when the character is either alphabet or number.
print("isdigit:",'10'.isdigit()) # True - when the character is digit (int).
print("isdigit:",'10.5'.isdigit()) # False
print("isnumeric:",'10'.isnumeric()) # True
print("title:",'Hello'.istitle())# True
print("lower:",'a'.islower()) # True - check the lowercase
print("upper:",'A'.isupper()) # True
print("space:",' '.isspace()) # True


