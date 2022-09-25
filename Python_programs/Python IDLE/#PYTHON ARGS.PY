                     #PYTHON *ARGS WITH EXERCISE

   # "*"-OPERATOR
   #WITH THE HELP OF THIS OPERATOR(*), WE CAN PASS MULTIPLE ARGUMENT TO A FUNCTON.
   #MAKE FLEXIBLE FUNCTION
  ##IT TAKES THE ARGUMENTS IN THE FORM OF TUPLE.
   
   #"args"-is just as a variable names, you can change it, whatever name you want.
   #WE WRITES "args" BECAUSE IT'S GLOBLY USED/WRITTEN.

#EXAMPLE
"""
def nums(*args):
    print(args)                     #(1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(type(args))               #<class 'tuple'>
nums(1,2,3,4,5,6,7,8,9)
"""

#ADD MULTIPLE NUMBERS
"""
def nums(*args):
    total=0
    for i in args:
        total += i
    return total
print(nums(1,2,3,4,5,6,7,8,9))      #45
"""
#LIKE THIS WE CAN PERFORM SUBS, MUL & DIV..............


         #ARGS WITH NORMAL PARAMETERS

#TRY TO UNDERSTAND WITH FOLLOWING EXAMPLES.
"""
#I.
def nums(num1,*args):   
    print(num1)                      #2
    print(args)                      #(3, 4, 5, 6): NOW ARGS CONTAINS ONLY THIS.
    mul=1
    for i in args:
        mul *= i
    return mul
print(nums(2,3,4,5,6))               #360

#II.
def nums(num1,num2,num3,*args):   
    print(num1)                      #2
    print(num2)                      #3
    print(num3)                      #4
    print(args)                      #(5, 6): NOW ARGS CONTAINS ONLY THIS.
    mul=1
    for i in args:
        mul *= i
    return mul
print(nums(2,3,4,5,6))               #30

##III.
def nums(*args):   
    print(args)                      #()
    mul=1
    for i in args:
        mul *= i
    return mul
print(nums())                        #1
       #YET WE DIDN'T PASS ANYTHING INTO nums() fn, STILL WE DIDN'T GOT AN ERROR.

#IV.
def nums(num1,*args):   
    print(args)                      
    mul=1
    for i in args:
        mul *= i
    return mul
print(nums())                #TypeError: nums() missing 1 required positional argument: 'num1'

#V.
def nums(num1,num2,*args):   
    print(args)                      
    mul=1
    for i in args:
        mul *= i
    return mul
print(nums())                #TypeError: nums() missing 2 required positional arguments: 'num1' and 'num2'
"""

#CONCLUSION: WE ARE FREE, EITHER PASS OR DON'T PASS ANY ARGUMENT TO "*" OPERATOR, WHILE CALLING THE fn.
#BUT FOR OTHERS i.e. num1,num2....WE MUST HAVE TO PASS ARGUMENT FOR THEM, WHILE CALLING THE fn.



  #WE CAN'T CHANGE THE POSITION OF "*args" PARAMETER, WHILE DEFINING THE fn.IT HAS FIXED POSITION AT THE LAST.
"""
def nums(*args,num1):   
    print(args)                      
    mul=1
    for i in args:
        mul *= i
    return mul
print(nums(1,2,3,4,5,6))    #TypeError: nums() missing 1 required keyword-only argument: 'num1'

  #ERROR BCOZ ALL THE ARGUMENTS HAS BEEN CONVERTED INTO TUPLE, NOTHING RAMAINS FOR "num1", DUE TO "*args" FIRST POSITION.
  

def nums(*args,num1):   
    print(args)                      
    mul=1
    for i in args:
        mul *= i
    return mul
print(nums())                #TypeError: nums() missing 1 required keyword-only argument: 'num1'
"""



         #"*args" AS A ARGUMENT: "TO UNPACK A LIST OR TUPLE".

#UNPACK A LIST
"""
def nums(*args):   
    print(args)              #([2, 3, 4, 5],)                   
    mul=1
    for i in args:
        mul *= i
    return mul
num1=[2,3,4,5]
print(nums(num1))            #[2, 3, 4, 5]: passed list*1=passed list
                             #BECAUSE LIST WAS UNPACKED
                            

def nums(*args):   
    print(args)              #(2, 3, 4, 5)                   
    mul=1
    for i in args:
        mul *= i
    return mul
num1=[2,3,4,5]
print(nums(*num1))           #120
      #NOW IT'S UNPACKED.
"""

#UNPACK A TUPLE

def nums(*args):   
    print(args)              #((2, 3, 4, 5),)                   
    mul=1
    for i in args:
        mul *= i
    return mul
num1=(2,3,4,5)               
print(nums(num1))            #(2, 3, 4, 5): passed tuple*1=passed tuple
                             #BECAUSE LIST WAS UNPACKED

def nums(*args):   
    print(args)              #(2, 3, 4, 5)                   
    mul=1
    for i in args:
        mul *= i
    return mul
num1=(2,3,4,5)               #YOU MAY AVOID THIS LINE, SEE BELOW METHOD.          
print(nums(*num1))           #120
      #NOW IT'S UNPACKED.
      

def nums(*args):   
    print(args)              #(2, 3, 4, 5)                   
    mul=1
    for i in args:
        mul *= i
    return mul
print(nums(*(2,3,4,5)))


"""
#problem
def sqrt(i,*args):
    if args:
        a=[j**i for j in args]
    else:
        print("you didn't enter anything")
    return a
#n=int(input("enter a no"))
x=int(input("enter a no"))
nums=list(range(1,x))
print(sqrt(3,*nums))
"""














































































































