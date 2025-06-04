
s="AbcDe 1234"
print("s=",s)
for i in range(0,len(s)):
    if s[i].islower():
        print("Lower:",s[i])
    elif s[i].isupper():
        print("Upper:",s[i])
    elif s[i].isdigit ():
        print("Digit:",s[i])
    elif s[i].isspace():
        print("Space:",s[i])

print("alpha:",s.isalpha())
print("alnum:",s.isalnum())


# Password Pattern

s=input("Enter The Password:")
u,sp,n=0,0,0
for i in range(0,len(s)):
    if s[i].isupper():
        u=u+1
    elif s[i].isdigit():
        n=n+1
    elif s[i]=='$' or s[i]=='@' or s[i]=='*':
        sp=sp+1
    else:
        pass

if u>=1 and n>=1 and sp==1:
    print("Valid Password")
else:
    print("Not Valid")
    

'''
# PAN Card Checking #
s=input("Enter The Pan No:")
a,b=0,0
if len(s)==10:
    for i in range(0,5):
        if s[i].isupper() or s[i].islower():
            a=a+1
    for j in range(5,9):
        if s[j].isdigit():
            b=b+1
    if a==5 and b==4 and (s[9].isupper() or s[9].islower()):
        print("Valid Pan")
    else:
        print("Invalid pan")
else:
    print("Invalid pan")

'''
# Login Example #

user=input("Enter The Username:")
passwd=input("Enter The Password:")
if user=="besant" and passwd=="Tech":
    print("Login Successful")
else:
    print("Invalid Login")


# Palindrome #

s=input("Enter The String:")
s1=s[::-1]
print(s1)
if s==s1:
    print("Palindrome")
else:
    print("Not palindrome")
    

# Split Example #

s="Red Shirt,Green Shirt,Blue Shirt"
shirts=s.split(",")
print(shirts)
for i in shirts:
    print(i)

shirts2=s.split(",",1)
print(shirts2)

'''

# Vowels Checking #
s=input("Enter The String:")
'''
for i in range(0,len(s)):
    if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
        print(s[i])

count=0
for i in range(0,len(s)):
    if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
        count=count+1
print("no.of vowels:",count)


print("a=",s.count('a',0,len(s)))
print("e=",s.count('e',0,len(s)))
print("i=",s.count('i',0,len(s)))
print("o=",s.count('o',0,len(s)))
print("u=",s.count('u',0,len(s)))
      

