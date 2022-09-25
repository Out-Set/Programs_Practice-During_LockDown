                            #LIST COMPREHENSION WITH EXAMPLES

            #WITH THE HELP OF LIST COMPREHENSION, WE CAN CREATE OF LIST IN ONE LINE.

     #EXAMPLES......

 #I.PRINT SQUARE OF N NO.

#BY SIMPLE MRTHOD
"""
n=int(input("enter n"))  #n=11
square=list(range(1,n))
square1=[]
for i in square:
      square1.append(i**2)
print(square1)                           #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
#BY LIST COMPREHENSION
"""
n=int(input("enter n"))  #n=11
square=[i**2 for i in range(1,n)]
print(square)                            #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""


 #II.PRINT -VE OF N NO.

#BY SIMPLE METHOD
"""
list=[1,2,3,4,5,6,7,8,9,10]
list1=[]
for i in list:
    list1.append(-i)
print(list1)                             #[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
"""
#BY LIST COMPREHENSION
"""
list=[-i for i in range(1,11)]
print(list)                              #[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
"""   


 #III.FIRST LETTER OF EVERY WORD, PRESENT IN A LIST.
"""
#BY SIMPLE METHOD
name=["Sawan","divya","Ankur"]
first=[]
for i in name:
    first.append(i[0])
print(first)                             #['S', 'd', 'A']
"""
#BY LIST COMPREHENSION
"""
name=["Sawan","divya","Ankur"]
first=[names[0] for names in name]
print(first)                             #['S', 'd', 'A']
"""


 #IV.REVERSE THE EVERY STRINGS INSIDE THE LIST
"""
name=["Sawan","divya","Ankur"]
revstr=[a[::-1] for a in name]
print(revstr)                            #['nawaS', 'ayvid', 'ruknA']
"""
  #using function
"""
def revstr(l):
    return [a[::-1] for a in l]    
print(revstr(["Sawan","divya","Ankur"])) #['nawaS', 'ayvid', 'ruknA']
"""



      #LIST COMPREHENSION WITH "IF-STATEMENT"

 #I.FILTER ODD & EVEN NUMBERS
#BY SIMPLE METHOD
"""
list=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)                             #[2, 4, 6, 8, 10]
print(odd)                              #[1, 3, 5, 7, 9]
"""
#BY LIST COMPREHENSION
"""
list=[1,2,3,4,5,6,7,8,9,10]
odd=[n for n in list if n%2!=0]
print(odd)                                  #[1, 3, 5, 7, 9]
even=[n for n in list if n%2==0]
print(even)                                 #[2, 4, 6, 8, 10]
    #or
odd=[i for i in range(1,11) if i%2!=0]
print(odd)                                  #[1, 3, 5, 7, 9]
even=[n for n in range(1,11) if n%2==0]
print(even)                                 #[2, 4, 6, 8, 10]
"""


 #II.FIND THE NUMBERS WHOSE TYPE IS INT OR FLOAT, in the form of string.
#BY SIMPLE METHOD
"""
list=["sawan",1.0,1,2,34,5]
l=[]
for i in list:
    if type(i)==int or type(i)==float:
        l.append(i)
print(l)
"""
#BY LIST COMPREHENSION
"""
list=["sawan",1.0,1,2,34,5]
l=[str(i) for i in list if (type(i)==int or type(i)==float)]
print(l)                                    #['1.0', '1', '2', '34', '5']

      #YOU CAN ALSO DO IT FOR STRING...& AND CAN CONVERT THE O/P INTO ANY FORM.
"""




      #LIST COMPREHENSION WITH "IF-ELSE STATAMENT"

 #I.FILTER ODD NO WITH MULTIPLE OF "-1", & EVEN NO MULTIPLE OF "2".
#BY SIMPPLE METHOD
"""
list=[1,2,3,4,5,6,7,8,9,10]
list1=[]
for i in list:
    if i%2==0:
        list1.append(2*i)
    else:
        list1.append(-i)
print(list1)                                #[-1, 4, -3, 8, -5, 12, -7, 16, -9, 20]
"""
#BY LIST COMPREHENSION
"""
list=[1,2,3,4,5,6,7,8,9,10]
list1=[i*2 if (i%2==0) else (-i) for i in list]
print(list1)                                #[-1, 4, -3, 8, -5, 12, -7, 16, -9, 20]
"""



      #LIST COMPREHENSION IN NESTED LIST

  #CREATE A NESTED 2D LIST
#BY SIMPLE METHOD
"""
list=[]
for i in range(3):
    list.append([1,2,3])
print(list)                                 #[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
"""
#BY LIST COMPREHENSION
"""
list=[[i for i in range(1,4)] for j in range(3)]
print(list)                                 #[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
      # YOU CAN WRITE "i" AT BOTH THE PLACE
list=[[i for i in range(1,4)] for I in range(3)]
print(list)                                 #[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
"""

















































