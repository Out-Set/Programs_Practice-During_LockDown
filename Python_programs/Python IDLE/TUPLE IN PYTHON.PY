                    #TUPLE EXERCISE
#TUPLE IS A COLLECTION WHICH IS ORDERED,CAN STORE ANY DATA TYPE, ARE FASTER THAN LISTS AND IMMUTABLE.

#CREATING A TUPLE: PYTHON TUPLES ARE WRITTEN WITH ROUND BRACKETS/PARENTHESIS.
  #i.e. thistuple=("apple","banana",1,2,2.3,4.5,"23")


           #ACCESS TUPLE ITEMS
#1.USING SLICING: RANGE OF INDEXES & RANGES OF +VE/-VE INDEXES [START INDEX : END INDEX : SEPARATION]
"""
thistuple=("apple","banana",1,2,2.3,4.5,"23")
print(thistuple[1])           #banana
print(thistuple[-1])          #23
print(thistuple[1:5])         #('banana',1,2,2.3)
print(thistuple[-1:-6:-2])    #('23',2.3,1)
print(thistuple[1:6:3])       #('banana',2.3)
print(thistuple[-1:-5])       #()
print(thistuple[::-1])        #('23',4.5,2.3,2,1,'bananaa','apple')
"""


          #CHANGE TUPLE VALUES: SINCE WE KNOW THAT TUPLES ARE IMMUTABLE, SO CONVERT IT INTO A LIST TO BO ABLE TO CHANGE IT.
"""
thistuple=("apple","banana",1,2,2.3,4.5,"23")
y=list(thistuple)             #NOW IT HAS BEEN CONVERTED INTO LIST YOU CAN PERFORM ANY OPERATION
y[1]="guava"
print(y)                      #['apple', 'guava', 1, 2, 2.3, 4.5, '23']   because it's still list we didn't interchanged into tuple
x=tuple(y)
print(x)                      #('apple', 'guava', 1, 2, 2.3, 4.5, '23')   we have converted list into tuple
"""


          #LOOP THROUGH A TUPLE
"""
thistuple=("apple","banana",1,2,2.3,4.5,"23")
for i in thistuple:
    print(i)
"""


          #CREATE TUPLE 'WITH ONE ELEMENT': ADD A "COMMA" AFTER THE ITEM,UNLESS PYTHON WON'T RECOGNISE THE VARIABLE AS A TUPLE, IT WILL READ THAT AS A SIMPLE DATA TYPE.
"""
a=(1)
print(type(a))               #<class 'int'>
b=('word')
print(type(b))               #<class 'str'>

   #BUT WHEN WE ADD A "COMMA" AFTER ITEM THEN......
a=(1,)
print(type(a))               #<class 'tuple'>
b=('word',)
print(type(b))               #<class 'tuple'>
"""


          #TUPLE WITHOUT PARENTHESIS
"""
a="apple","banana","23",3,4,4.5
print(type(a))               #<class 'tuple'>
"""


          #TUPLE UNPACKING: "NO OF ITEMS INSDE THE TUPLE == NO. OF VARIABLE" TO UNPACK, OTHERWISE YOU WILL GET AN ERROR.
"""
a=("sawan","kuamr","prajapati")
first_name,middle_name,last_name=(a)
print(first_name)            #sawan
print(middle_name)           #kumar
print(last_name)             #prajapati

    #BUT IF ....."NO OF ITEMS INSDE THE TUPLE > NO. OF VARIABLE"
#a=("sawan","kuamr","prajapati")
#first_name,middle_name=(a)                       #ValueError: too many values to unpack (expected 2)

    #BUT IF ....."NO OF ITEMS INSDE THE TUPLE < NO. OF VARIABLE"
a=("sawan","prajapati")
first_name,middle_name,last_name=(a)              #ValueError: not enough values to unpack (expected 3, got 2)
"""


           #LIST INSIDE TUPLE
"""
a=("apple","banana",["guava","cherry","lichi"])
print(a[2].pop())             # O/P  lichi: POPPED ELEMENT
a[2].pop()
print(a)                      #('apple', 'banana', ['guava'])

a=("apple","banana",["guava","cherry","lichi"])
a[2].append('mango')
print(a)                      #('apple', 'banana', ['guava', 'cherry', 'lichi', 'mango'])
"""


           #MIN AND MAX FUNCTION
"""
a=(12,3,45,6,78,45,90)
print(min(a))                 #3
print(max(a))                 #90
b=("apple","we","i")
print(min(b))                 #i
print(max(b))                 #apple
"""


            #INTERCHANGING OF TUPLE INTO "LIST" AND "SRRING"
"""
a=(1,2,3,4,5,6,7)
str_tuple=str(a)
print(str_tuple)              #(1, 2, 3, 4, 5, 6, 7)   actualitive it's in the form of string....   "(1, 2, 3, 4, 5, 6, 7)"
print(type(str_tuple))        #<class 'str'>
                 
a=(1,2,3,4,5,6,7)
list_tuple=list((a))
print(list_tuple)             #[1, 2, 3, 4, 5, 6, 7]


    #OR
a=str((1,2,3,4,5,6,7))
print(a)                      #(1, 2, 3, 4, 5, 6, 7)   actualitive it's in the form of string....   "(1, 2, 3, 4, 5, 6, 7)"
print(type(a))                #<class 'str'>

a=list((1,2,3,4,5,6,7))
print(a)                      #[1, 2, 3, 4, 5, 6, 7]
"""



             #CHECK IF ITEM EXISTS IN TUPLE: USING "IN" KEYWORD
"""
a=('apple','banana','cherry')
if 'apple' in a:
    print("apple is present")
else:
    print("not present")
"""


             #TUPLE LENGTH: USING LEN() METHOD.
"""
a=('apple','banana','cherry')
print(len(a))                #3
"""



             #JOIN TWO TUPLE: USING "+" OPERATOR.
"""
a=('apple','banana','cherry')
b=("GUAVA","GRAPES","LICHI")
c=a+b
print(c)                       #('apple', 'banana', 'cherry', 'GUAVA', 'GRAPES', 'LICHI')
"""



             #ADD AND REMOVE ITEMS THROUGH A TUPLE: YOU CAN'T ADD AND REMOVE ITEMS TO A TUPLE, THIS WILL RAISE AN ERROR, BUT YOU CAN "DELETE IT COMPLETELY" USING "DEL KEYWORD".

a=('apple','banana','cherry')
del a
print(a)                       #NameError: name 'a' is not defined...because this tuple no longer exists.




























































































