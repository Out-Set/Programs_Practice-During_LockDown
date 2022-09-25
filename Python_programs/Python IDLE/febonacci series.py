"""
#BY SIMPLE METHOD
n=int(input("enter the n"))
a,b,i,c=0,1,1,0
print(a)
print(b)
while i<=n:
    c=a+b
    print(c)
    a=b
    b=c
    i+=1
"""

#BY FUNCTION
def fibb(n):
    a=b=0
    c=d=1
    print(a)
    print(c)
    while d<=n:
        b=a+c
        print(c)
        a=c
        c=b
        i+=1
e=int(input("enter the no uup to which you waana fibbonaci series\n")
 print(fibb(e))
        
#another method
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

def fib_rec(n):
    '''recursive fibnacci'''
    if(n<=1):
        return n
    else:
        return fib_rec(n-1)+fib_rec(n-2)

def fib_iter(n):
    '''iterative fibonacci'''
    cur,nxt=0,1
    for k in range(n):
        cur,nxt=nxt,cur+nxt
    return cur

def fib_upto(n):
    '''given n, return list of fibonacci numbers<=n'''
    cur,nxt=0,1
    lst=[]
    while(cur<n):
        lst.append(cur)
        cur,nxt=nxt,cur+nxt
    return lst
