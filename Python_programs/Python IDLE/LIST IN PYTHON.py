                                        #LIST'S OPERATIONS & EXERCISE


#OPERATIONS ON LISTS

"""
list=[1,2,3,4,5,3.4,6.2,"sawan","prajapati",None]
print(list)
print(list[5])
print(list[-3])
print(list[3:7])                  #IN SLICING LAST INDEX DOSEN'T INCLUDES ONLY 1ST AND MIDDLE ELEMENTS INCLUDES
print(list[-8:-2])
"""

#CHANGING ITEMS NAMES IN LISTS
"""
a=["apple","banana","grapes"]
print(a)
a[1:]=["guava","cherry"]
print(a)
a[:2]=["guava","cherry"]
print(a)
a[0:2]=["guava","cherry"]
print(a)
"""



      #INTERCHANGING OF LISTS INTO "TUPLEE & STRING"
"""
a=str([1,2,3,4,5,6,7])
print(a)                           # o/p...[1, 2, 3, 4, 5, 6, 7]  but it's actiuallly in this form "[1, 2, 3, 4, 5, 6, 7]" as a string
print(type(a))                     #<class 'str'>

a=tuple([1,2,3,4,5,6,7])
print(a)                           # o/p...(1, 2, 3, 4, 5, 6, 7)  as a tuple
"""



      #RANGE FUNCTION: IT IS USED TO CREATE THE LISTS
"""
num=list(range(1,11))
print(num)         #o/p  [1,2,3,4,5,6,7,8,9,10]
"""



     #ADD ITEMS TO A LIST
# 1.USING APPEND() METHOD: ADD THE ITEMS IN THE LAST
"""
list=["apple","banana","grapes"]
list.append("orange")              
print(list)
#list.append("papaya","guava")     #ERROR: BECAUSE APPEND TAKES ONLY ONE ARGUMENT, TWO IS GIVEN
#print(list)
"""

# 2.USING INSERT() METHOD: ADD THE ELEMENTS AT SPECIFIED POSITION
"""
list=["apple","banana","grapes"]
list.insert(1,"orange")              
print(list)
"""



    #REMOVE ITEMS TO A LIST
# 1.REMOVE() METHOD: REMOVES THE SPECIFIED ITEMS
"""
list=["apple","banana","grapes","guava","orange","cherry"]
print(f"MY LIST IS: {list}")
list.remove("banana")
print(list)
"""

# 2.POP() METHOD: REMOVES THE SPECIFIED INDEXES
"""
list=["apple","banana","grapes","guava","orange","cherry"]
list.pop() #IF NO ARGUMENTS IS GIVEN IT REMOVES THE LAST ITEMS
print(list)

list=["apple","banana","grapes","guava","orange","cherry"]
list.pop(-1)                       
print(list)

list=["apple","banana","grapes","guava","orange","cherry"]
list.pop(5)
print(list)
"""

# 3.DEL KRYWORDS:
"""
    # I.CAN REMOVE THE SPECIFIED INDEX
list=["apple","banana","grapes","guava","orange","cherry"]
del list[4]
print(list)

    # II. CAN DELETE THE LIST COMPLETELY
list=["apple","banana","grapes","guava","orange","cherry"]
del list
"""

# 4.CLEAR() METHOD: EMPTIES THE LIST JUST LIKE DEL KEYWORDS
"""
list=["apple","banana","grapes","guava","orange","cherry"]
list.clear()
"""



    #JOIN TWO LISTS
# 1.USING '+' OPERATOR
"""
list1=[1,2,3]
list2=['a','b','c']
list3=list1+list2
print(list3)
"""

# 2.APPPEND() METHOD:
"""
   #I.APPEND ALL THE ELEMENTS FROM LIST1 TO LIST2 ONE BY ONE
list1=[1,2,3]
list2=['a','b','c']
for x in list2:
    list1.append(x)
print(list1)

   #II."LIST INSIDE THE LIST": IT APPEND THE ONE LIST INTO OTHERS ONE 
list1=[1,2,3]
list2=['a','b','c']
list1.append(list2)
print(list1)
"""

# 3.EXTEND() METHOD: ADD THE ITEMS OF LIST2 AT THE END OF LIST1
"""
list1=[1,2,3]
list2=['a','b','c']
list1.extend(list2)
print(list1)
"""



#CHECK IF ITEM EXISTS IN LIST
"""
list=["apple","banana","grapes","guava","orange","cherry"]
if "apple" in list:
    print("APPLE is present")
"""



#LIST LENGTH [using len() function): DETERMINES THE NO OF ITEMS PRESENT IN A LIST
"""
list=["apple","banana","grapes","guava","orange","cherry"]
print(len(list))
list2=['a','b','c']
print(len(list2))
"""




    #SOME IMPORTANT METHODS IN LISTS
# 1.COUNT() METHODS: COUNTS THE NO OF TIME, ANY ITEMS APPEARS IN THE LISTS
"""
list2=['a','b','c','d','a']
print(list2.count('a'))

list=["apple","banana","grapes","guava","orange","cherry","apple"]
print(list.count("apple"))
"""

# 2.SORT() METHOD: IT ARRANGE THE LIST ITEMS INTO ACCCENDING ORDER #IT'S CHANGES THE ORDER PERMANENTLY OF LIST ITEMS
"""
list=["apple","banana","grapes","guava","orange","cherry","carrot"]
list.sort()
print(list)

list2=['a','z','d','f','x','u','b']
list2.sort()
print(list2)

list3=[1,4,3,6,8,9,4,33,55,111,99,77,567,980,34,45]
list3.sort()
print(list3)
"""

# 3.SORTED() FUNCTION: IT ARRANGE THE LIST ITEMS INTO ACCCENDING ORDER #BUT NOT PERMANENTLY
"""
list=["apple","banana","grapes","guava","orange","cherry","carrot"]
print(sorted(list))    #SORTED LIST
print(list)            #NOT SORTED LIST

list3=[1,4,3,6,8,9,4,33,55,111,99,77,567,980,34,45]
print(sorted(list3))    #SORTED LIST
print(list3)            #NOT SORTED LIST
"""




      #COPY A LIST
# 1.WITH COPY() METHOD
"""
list=["apple","banana","grapes","guava","orange","cherry","carrot"]
list1=list.copy()     #LIST HAS BEEN COPIED INTO LIST1
print(list1)
"""

# 2.WITH LIST() METHOD
"""
mylist=["apple","banana","grapes","guava","orange","cherry","carrot"]
list1=list(mylist)
print(list1)
"""




        #LIST INSIDE LIST
# 2D LIST
"""
matrix1=[[1,2,3],[4,5,6],[7,8,9]]
  #ACCESSING INSIDES LIST
print(matrix1[0])
print(matrix1[2])

  #ACCESSING ELEMENTS INSIDE LIST OF LIST
print(matrix1[0][2])
print(matrix1[2][2])

  #ACCESSING EVERY SINGLE ELEMENTS
for sublist in matrix1:
    for i in sublist:
        print(i)
"""

# 3D LIST
"""
matrix2=[[[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16],[17,18,19]],[[21,22,23],[24,25,26],[27,28,29]]]
   #ACCESSING INSIDES LIST
print(matrix2[0])
print(matrix2[2][2])

   #ACCESSING ELEMENTS INSIDE LIST OF LIST OF, LIST
print(matrix2[0][2][2])
print(matrix2[2][2][1])

   #ACCESSING EVERY SINGLE ELEMENTS
for sublist in matrix2:
    for i in sublist:
        print(i)
"""




      #INDEX() METHOD: IT IS USED TO FIND THE POSITION OF ANY PARTICULAR ITEM/ELEMENTS IN LISTS
"""
list0=[1,2,3,4,5,6,7,8,9]
print(list0.index(7))

list1=['a','s','g','r''q']
print(list1.index('g'))

list3=["apple","banana","grapes","guava","orange","cherry","carrot"]
print(list3.index("guava"))
"""

 #IF AN ELEMENTS OCCURS MULTIPLE TIMES THEN......IT RETURN THE POSITION WHEN IT APPEARS FIRST....BECAUSE BY DEFAULT IT START FINDING POSITION FROM ZERO
"""
list4=[1,2,3,4,5,6,1,7,8,9,1]
print(list4.index(1))       #RETURN ONLY '0' POSITION   BUT WE CAN COUNT ANOTHER ONE.....
print(list4.index(1,3))     #NOW IT WILL RETURN '6'....BECAUSE WE HAVE GIVEN THE START POSITION '3', SO IT WILL FIND THE POSITION OF '1' FROM THE '3RD' POSITION

 #YOU CAN SEARCH IN B/W INDEXES MEANS YOU CAN ALSO GIVE END INDEX/POSITION
list4=[1,2,3,4,5,6,1,7,8,9,1]
print(list4.index(1,5,9))
print(list4.index(1,1,6))   #VALUE ERROR: 1 IS NOT IN LIST
"""



                           #EXERCISE IN LISTS

# 1.DEFINE A FUNCTION WHICH WILL TAKE LIST AS A INPUT AND RETURN US 'SQUARE' OF LIST.
"""
num=list(range(1,11))
def square(l):
    sqrt=[]
    for i in l:
        sqrt.append(i**2)
    return sqrt
print(square(num))
"""


# 2.DEFINE A FUNCTION WHICH WILL TAKE LIST AS A INPUT AND RETURN US 'NEGATIVE' OF LIST.
"""
list=[1,2,3,4,5]
def neg(a):
    negative=[]
    for i in a:
        negative.append(-i)
    return negative
print(neg(list))
"""


# 3.DEFINE A FUNCTION WHICH WILL TAKE LIST OF NO AS A INPUT AND RETURN US 'REVERSE' OF LIST.
"""
 #I.USING SLICING METHOD
num=list(range(1,11))
def rev(l):
    return l[::-1]
print(rev(num))


 #III.USING REVERSE METHOD
def rev(l):
    l.reverse()
    return l
list1=list(range(1,11))
print(rev(list1))


 #III.USING POP & APPEND METHOD
def rev(l):
    list2=[]
    for i in range(len(l)):
        popped_ele=l.pop()
        list2.append(popped_ele)
    return list2
list1=list(range(1,11))
print(rev(list1))
"""


# 4.DEFINE A FUNCTION WHICH WILL TAKE LIST OF WORDS AS A INPUT AND RETURN US 'REVERSE' OF LIST, ALSO 'REVERSE EVERY WORD' INSIDE LIST.
"""
a=['abc','wer','ghj']
def rev(l):
    rev_list=[]
    for i in l:
        rev_list.append(i[::-1])
    return rev_list
print(rev(a))
"""


# 5.FILTER ODD & EVEN, FROM A LIST & PRINT O/P WITHIN A LIST.....i.e. [[EVEN....],[ODD....]]
"""
list0=list(range(1,11))
def odd_even(l):
    even=[]
    odd=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    #return even, odd             o/p  ([2,4,6,8,10],[1,3,5,7,9])  INTO PARANTHESIS
    output=[odd,even]        #NOW O/P  [[1,3,5,7,9],[2,4,6,8,10]]   INTO LIST
    return output      
print(odd_even(list0))    
"""


# 6.DEFINE A FUNCTION WHICH WILL TAKE TWO LIST AS A INPUT AND RETURNS, THE COMMON ITEMS/ELEMENTS B/W THEM.
"""
list0=list(range(1,11))
list1=list(range(6,12))
def common(l,m):
    common_item=[]
    for i in l:
        if i in m:
            common_item.append(i)
    return common_item
print(common(list0,list1))      #0/p  [6,7,8,9,10]
"""


# 7.ADD TWO 2D MATRIX
"""
mat1=[[1,2,3],[4,5,6],[7,8,9]]
mat2=[[1,2,3],[4,5,6],[7,8,9]]
sum=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(mat1)):
    for j in range(len(mat2)):
        sum=mat1[i][j]+mat2[i][j]
print(sum)
"""


# 8.DEFINE A FUNCTION WHICH TAKES LIST AS A INPUT, AND RETURN US THE DIFFERENCE OF 'GREATEST-SMALLEST' NO ISNSIDE THE LIST
"""
a=[34,45,2,67,98,5,68,23,12]
def diff(l):
    return max(l)-min(l)
print(diff(a))                      #o/p '96' i.e. 98-2
"""


# 9.DEFINE A FUNCTION WHICH TAKES LIST AS A INPUT, AND RETURN US THE THE 'SUBLISTS' PERSENT IN THE LIST.

def sublist_counter(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count
a=[[1,2,3],4,5,6,[5,6],6,[7,8,9]]
print(sublist_counter(a))         #o/p  3











































































































      

    









































































