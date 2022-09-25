                     #PYTHON "*ARGS" & "**KWARGS" WITH EXAMPLES

   # "*"-OPERATOR
   #WITH THE HELP OF THIS OPERATOR(*), WE CAN PASS MULTIPLE ARGUMENT TO A FUNCTON.
   #MAKE FLEXIBLE FUNCTION
  ##IT TAKES THE ARGUMENTS IN THE FORM OF TUPLE.
   
   #"args"-is just as a variable names, you can change it, whatever name you want.
   #WE WRITES "args" BECAUSE IT'S GLOBLY USED/WRITTEN.
   

                #"*args" AS APARAMETER

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
num1=[2,3,4,5]               #YOU MAY AVOID THIS LINE, SEE BELOW METHOD.
print(nums(*num1))           #120
      #NOW IT'S UNPACKED.


def nums(*args):   
    print(args)              #(2, 3, 4, 5)                   
    mul=1
    for i in args:
        mul *= i
    return mul
print(nums(*[2,3,4,5]))      #120      
"""

#UNPACK A TUPLE
"""
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
print(nums(*(2,3,4,5)))      #120
"""


                  #"**kwargs" WITH EXAMPLES


   # "**"-double OPERATOR
   #WITH THE HELP OF THIS OPERATOR(*), WE CAN PASS MULTIPLE ARGUMENT TO A FUNCTON.
   #MAKE FLEXIBLE FUNCTION
  ##IT TAKES THE ARGUMENTS IN THE FORM OF DICTIONARY.
   
   #"kwargs"-is just as a variable names, you can change it, whatever name you want.
   #WE WRITES "kwargs" BECAUSE IT'S GLOBLY USED/WRITTEN.

   
               #"**kwargs" AS A PARAMETER
   
#EXAMPLE
"""
def func(**kwargs):
    print(kwargs)                     #{'first_name': 'sawan', 'last_name': 'prajapati'}
    print(type(kwargs))               #<class 'dict'>
func(first_name="sawan",last_name="prajapati")
"""

"""
def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}: {v}")
func(first_name="sawan",last_name="prajapati")   #first_name: sawan
                                                 #last_name: prajapati
"""

"""
def func(name,**kwargs):
    for k,v in kwargs.items():
        print(f"{k}: {v}")
func(first_name="sawan",last_name="prajapati")   #TypeError: func() missing 1 required positional argument: 'name'
                                                 #WE DIDN'T PASS ANY NAME ARG. ON THE CALLING OF fn.
                                                 #YOU MUST HAVE TO PASS IT, ELSE YOU WILL GET ERROR.
                                                 #SEE BELOW EXAMPLE, WHERE IT'S PASSED.
"""

"""
def func(name,**kwargs):
    print(name)                                  #Ankur
    for k,v in kwargs.items():
        print(f"{k}: {v}")
func("Ankur",first_name="sawan",last_name="prajapati")  #first_name: sawan
                                                        #last_name: prajapati
"""


 #DICTIONARY UNPACKING
"""
def func(**kwargs):                                  
    for k,v in kwargs.items():
        print(f"{k}: {v}")
d={'name':'sawan','age':23}                     ##YOU CAN AVOID THIS LINE, SEE BELOW EXAMPLE.
func(**d)                                       #name: sawan
                                                #age: 23
        #OR
def func(**kwargs):                                  
    for k,v in kwargs.items():
        print(f"{k}: {v}")                   
func(**{'name':'sawan','age':23})               #name: sawan
                                                #age: 23
"""


               #FUNCTION WITH ALL PARAMETERS

 #SEQUENCE: PADK means-(SIMPLE PARAMETER, *ARGS, DEFAULT PARAMETER, **KWARGS)
 #WE WILL HAVE TO FOLLOW THE ABOVE SEQUENCES, ELSE YOU WILL GET AN ERROR.
"""
def func(first_name,*args,last_name='unknown',**kwargs):
    print(first_name)
    print(last_name)
    print(args)
    print(kwargs)
func('sawan',1,2,3,a=1,b=2)          O/P   #sawan
                                           #unknown
                                           #(1, 2, 3)
                                           #{'a': 1, 'b': 2
"""

  #IF WE DISTURB THE SEQUENCES
"""
def func(*args,first_name,last_name='unknown',**kwargs):
    print(first_name)
    print(last_name)
    print(args)
    print(kwargs)
func('sawan',1,2,3,a=1,b=2)

              #TypeError: func() missing 1 required keyword-only argument: 'first_name'
"""



TRY THE EXERCISE SESSION 148 & 149 MUST































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














































































































