#PROGRAM TO PRINT N EVEN NATURAL NUMBERS
'''
n=int(input("enter the number"))
for i in range(0,2*n):
    if i%2==0:
        j=i
        print(j)
'''

#PROGRAM TO PRINT N EVEN NATURAL NUMBERS IN REVERSE ORDER
'''
n=int(input("enter the number"))
for i in range(2*n,0,-1):
    if i%2==0:
        j=i
        print(j)
'''     
    
#PROGRAM TO PRINT N ODD NATURAL NUMBERS
'''
n=int(input("enter the number"))
for i in range(0,2*n):
    if i%2!=0:
        j=i
        print(j)
        
'''
#PROGRAM TO PRINT N ODD NATURAL NUMBERS IN REVERSE ORDER
'''
n=int(input("enter the number"))
for i in range(2*n,0,-1):
    if i%2!=0:
        j=i
        print(j)
'''

#PROGRAM TO PRINT PRIME NUMBERS
n=int(input("enter the number"))
for i,n in enumerate(1,n):
    if i%n==0:
        print(i,end=" ")
