"""
def my_fun(x):
    return 5*x
print(my_fun(5))
print(my_fun((5+2)))
"""

"""
#country="India"
def my_fun(country="India"):
    print("myself from "+country)

"""

"""
def myfun(a,b):
    return a+b
a=int(input("enter first no"))
b=int(input("enter second no"))
total=a+b
print(total)
"""

"""
def myfun(c,d):
    return a+b
a=input("enter first string")
b=input("enter second string")
#total=a+b
print(myfun(a,b))
"""

"""
def add_three(a,b,c):
    print(a+b+c)       #return v/s print
add_three(5,5,5)
"""

"""
#last character
def last_char(a):
    return (a[-1])
print(last_char("sawan"))
"""

"""
#even odd
def even_odd(a):
    if a%2==0:
        return "even"
    else:
        return "odd"
b=int(input("enter a no"))
print(even_odd(b))
"""
"""        #OR
def even_odd(a):
    if a%2==0:
        return "even"
    return "odd"
b=int(input("enter a no"))
print(even_odd(b))
"""
"""        #OR
def even_odd(a):
    return a%2==0   #IT WILL RETURN TRUE IF EVEN ELSE ODD
b=int(input("enter a no"))
print(even_odd(b))
"""
 
"""
#returning multiple values
def add(a,b):
    return a+b,a-b,a//b,a*b,a%b,a**b
print(add(20,10))
"""

"""
#greatest no in b/w two
def lar(a,b):
    return a>b     #RETURN TRUE IF A>B ELSE FALSE
c=int(input("enter first no"))
d=int(input("enter second no"))
print(lar(c,d))
"""

"""
#GREATEST NO IN B/W THREE
def great(a,b,c):
    if a>b and a>c:
        return "A IS GREATEST"
    elif b>a and b>c:
        return "B IS GREATEST"
    else:
        c>a and c>b
        return "C IS GREATEST"
d=int(input("input A"))
e=int(input("enter B"))
f=int(input("enter C"))
print(great(d,e,f))
"""

