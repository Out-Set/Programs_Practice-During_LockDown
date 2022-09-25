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

def printHi():
    print("HI")

def __print__():
    print("1") 


'''to make it usable for commond line(cmd)'''
if __name__=="__main__":
    import sys
    print(fib_iter(int(sys.argv[i])))
