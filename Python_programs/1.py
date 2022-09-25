def fibonacci(n):
    a,b,c=0,1,0
    while True:
        if c>n:
            return
        yield a
        b=a+b
        a=b
        c+=1
        
it =fibonacci(10)
