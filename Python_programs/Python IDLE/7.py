'''
print("Second Number Pattern ")
lastNumber = 6
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")
'''

'''
n=int(input("enter a no"))
a,b=0,1
print(a,b,end=" ")
i=1
while i<=n:
    a,b=b,a+b
    print(b,end=" ")
    
    i+=1
'''

'''
def rec(n):
    print(n)
    i=1
    while i<=n:
        j=rec(n-1)
        return j    
print(rec(12))
'''
'''
def fact(n):
    if n==0:
        print("fact=1")
    if n<0:
        print("no fact for -ve values")
    i=1
    while i<n:
        fac=n*fact(n-1)
        return fac
    
print(fact(4))
'''

n=6
i=1
while i<n:
    f=






























