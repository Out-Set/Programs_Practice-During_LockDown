a="fizz"
b="buzz"
def fizzbuzz(n):
    for i in range(1,n+1):
        if i%3==0:
            print(a)            
        elif i%5==0:
            print(b)
        elif i%3==0 and i%5==0:
            print(a+b)    
        else:
            print(i)

fizzbuzz(15)
