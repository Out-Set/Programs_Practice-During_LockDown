                       #PYTHON LAMBDA EXPRESSION WITH EXERCISE

   # A LAMBDA FUNCTION IS SMALL ANONYMOUS FUNCTION.
   # LAMBDA EXPRESSION HAS NO NAME, SO THAT WE CALL IT "ANONYMOUS FUNCTION".
   # THIS TOPIC IS FIRSTLY EXPRESSED ONLY IN PYTHON, INSPIRING FROM PYTHON IT HAS COME IN JAVA & C++..
   # A LAMBDA fn CAN TAKE ANY NO OF ARGUMENT, BUT CAN HAVE ONLY ONE EXPRESSION.
   # THE EXPRESSION IS EXECUTED AND THE RESULT IS RETURNED.

#BY SIMPLE METHOD
"""
def add(a,b):
    return a+b
print(add(3,2))                 #5
"""

#BY LAMBDA METHOD
"""
add=lambda a,b : a+b
print(add(3,2))                 #5

mul=lambda a,b,c : a*b*c
print(mul(1,2,3))               #6
"""


  #ACTUALLY WE DON'T ASSIGN THE EXPRESSION OF LAMBDA FUNCTION INTO ANY VARIABLE(i.e. add, mul etc..)
  #IT'S JUST FOR UNDERSTANDING PURPOSE, YOU WILL SEE ABOUT IT FURTHER.


 #AS WE KNOW THAT, A LAMBDA FUNCTION IS ANONYMOUS(NO NAME) FUNCTION, MEANS IT WON'T HAVE A SPECIFIC NAME.
#PROOF:
"""
add=lambda a,b : a+b
mul=lambda a,b,c : a*b*c
print(add)                       #<function <lambda> at 0x0000026E27BB3AF8>
print(mul)                       #<function <lambda> at 0x000001CBAC623288>
                        #IT'S ONLY SHOWING THE LOCATION IN MEMORY, WHERE IT EXISTS.
                        #NOT ANY NAME, ONLY "LAMBDA"...<function <lambda>
"""

          #BUT IN FUNCTIONS....
"""
def add(a,b):
    return a+b
print(add)                       #<function add at 0x000001E92C273708>
                        #IT'S SHOWING THE fn NAME "add", AS WELL AS LOCATION.
"""

#SO IT'S PROOVED THAT, A LAMBDA FUNCTION IS ANONYMOUS(NO NAME) FUNCTION.



       #LAMBDA WITH IF-ELSE.

 #CHECK A STRING, WHETHER IT'S NUMBERS OF CHARACTERS (>5 OR <5).
#BY SIMPLE METHOD.
"""
def func(a):
    if len(a)>5:
        return True
    return False    
print(func('sawan_kuamr'))        #True
print(func('sawan'))              #False

     #OR     
def func(a):
    return len(a)>5
    
print(func('sawan_kuamr'))        #True
print(func('sawan'))              #False
"""

#BY LAMBDA METHOD.
"""
check=lambda a : True if len(a)>5 else False
print(check('sawan_kumar'))       #True
print(check('sawan'))             #False

      #OR
check=lambda a : len(a)>5 

print(check('sawan_kumar'))       #True
print(check('sawan'))             #False
"""    




                  #WHY USE LAMBDA FUNCTION ??
 #THE POWER OF LAMBDA IS BETTER SHOWN, WHEN YOU USE THEM AS AN ANONYMOUS fn INSIDE ANOTHER fn.

#SAY YOU HAVE A fn DEFINITION THAT TAKES ONE ARGUMENT, AND THAT ARGUMENT WILL BE MULTIPLIED WITH AN UNKNOWN NUMBER.
"""
def myfunc(n):
    return lambda a: a*n
#Use this fn definition to make a fn, that always double the number you send in.
mydoubler=myfunc(2)
print(mydoubler(11))              #22
"""



   #EXERCISE
#CHECK WHETHER NUMBER IS EVEN OR ODD.
"""
is_even=lambda a : a%2==0
print(is_even(4))                 #True
print(is_even(3))                 #False
"""

#RETURN THE LAST CHARACTER OF A STRING.
"""
last_char=lambda a : a[-1]
print(last_char('sawan'))         #n
"""

