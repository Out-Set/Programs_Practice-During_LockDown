                            #PYTHON SETS & EXERCISE

  # PYTHON SETS IS AN UNORDERED, UNINDEXED AND UNIQUE, WRITTEN IN CURLY BRACKETS.
  #YOU CAN STORE TYPE OF DATA IN SETS ONLY i.e. INTEGER,FLOAT AND STRING.

  
  #YOU CAN'T STORE TYPE OF DATA IN SETS i.e. LIST, TUPLE, DICTIONARY...
"""  
thisset={"apple","banana",1,2,3.4,4.5,{'name':'sawan'},[23,34],(21,67)}
print(thisset)           #TypeError: unhashable type: 'dict'       
"""

  #PYTHON IGNORES THE FLOATING VALUE: IF ANY INTEGER VALUE CONTAINING FLOATING VALUE ONLY ZERO.
"""
thisset={1,1.0,1.1,2,2.00,2.1,3,3.0,3.4,0.0,0.2,0.25}
print(thisset)           #{0.0, 1, 2, 3, 2.1, 1.1, 3.4, 0.2, 0.25}
                         #1.0=1, 2.0=2, 2.00=2, 3.0=3, 4.0=4 ...like this
"""
  
#UNORDERED: YOU CAN'T BE SURE IN WHICH OREDER THEY WILL APPEAR
"""
thisset={"apple","banana",1,2,3.4,4.5}
print(thisset)           #{1, 2, 3.4, 'apple', 4.5, 'banana'}  HERE ORDER HAS CHANGED.
"""

#UNINDEXED: DUE TO UNINDEXED YOU CAN'T ACCESS ITEMS thisset={"apple","banana",1,2,3.4,4.5}
"""
thisset={"apple","banana",1,2,3.4,4.5}
print(thisset[1])        #TypeError: 'set' object is not subscriptable
"""

#UNIQUE: THIS IS THE "MAIN ADVANTAGE" OF SETS THAT "NO ONE ELEMENTS WILL APPEAR MULTIPLE TIMES". IT'S ALSO KNOWN AS "REMOVE DUPLICATE".
"""
thisset={"apple","banana","apple",1,2,31,2,33,31,4,4,4,5,5,3.4,4.5,4.5,4.5}
print(thisset)           #{1, 2, 33, 4, 5, 3.4, 4.5, 'banana', 'apple', 31}
                         #nothing appering multiple times
  #SUPPOSE WE HAVE A LIST....

list1=[1,2,2,2,2,2,24,4,4,4,5,5,5,5,6,7,7,8,9,9,9,10]
set1=list(set(list1))
print(set1)              #[1, 2, 4, 5, 6, 7, 8, 9, 10, 24] 
"""



    #ACCESSING ITEMS: YOU CAN'T ACCESS ITEM TO ANY SETS.



#IF WITH IN: BUT YOU CAN ASK,WHETHER THIS ITEM IS PRESENT OR NOT.
"""
thisset={"apple","banana",1,2,3.4,4.5}
if "banana" in thisset:
    print("present")            #present
else:
    print("not present")
"""

    
    #LOOP THROUGH THE SETS
"""
thisset={"apple","banana",1,2,3.4,4.5} 
for x in thisset:
    print(x)                    #1
                                #2
                                #3.4
                                #4.5
                                #apple
                                #banana
"""


    #CHANGE ITEMS: ONCE A SET IS CREATED, YOU CAN'T CHANGE ITEMS, BUT YOU CAN ADD NEW ITEMS.


         #ADD ITEMS: YOU CAN ADD NEW ITEMS TO A SET.

 #I. ADD() METHOD: ADD AN/SINGLE ITEM TO A SET, USING ADD() METHOD.
"""
thisset={"apple","banana","GUAVA"}
thisset.add("orange")
print(thisset)              #{'orange', 'apple', 'GUAVA', 'banana'}

thisset.add("cherry")
print(thisset)              #{'orange', 'banana', 'GUAVA', 'cherry', 'apple'}

thisset.add("orange")
print(thisset)              #{'orange', 'banana', 'GUAVA', 'cherry', 'apple'}
                            #IT WON'T ADD ORANGE,, BCOZ IT'S ALREADY IN SET(THROUGH UNIQUE PROPERTY OF SETS).
"""

 #II. UPDATE() METHOD: ADD MULTIPLE ITEMS TO A SET, USING UPDATE() METHOD.

thisset={"apple","banana","GUAVA"}
thisset.update("orange","cherry","lichi")
print(thisset)




         #REMOVE ITEMS: REMOVE ANY ITEMS TO A SET.

 #I.REMOVE() METHOD
"""
thisset={"apple","banana","GUAVA"}
thisset.remove("apple")
print(thisset)             #{'banana', 'GUAVA'}

thisset.remove("lichi")
print(thisset)             #KeyError: 'lichi'
                           #RAISE AN ERROR IF ITEM IS NOT PRESENT
                           #IT CAN BE AVOIDED USING DISCARD() METHOD.
"""

 #II.DISCARD() METHOD
"""
thisset={"apple","banana","GUAVA"}
thisset.discard("apple")
print(thisset)             #{'banana', 'GUAVA'}

thisset.discard("lichi")
print(thisset)             #{'banana', 'GUAVA'}
                           #SINCE "LICHI" IS NOT PRESENT, YET IT DIDN'T "RAISE AN ERROR".
"""

 #III.POP() METHOD: ALTHOUGH THIS REMOVES THE LAST ITEM, BUT HERE IN SET, IS UNORDERED SO YOU WON'T KNOW WHAT ITEM GET REMOVED.
"""
thisset={"apple","banana","GUAVA"}
thisset.pop()
print(thisset)             #{'GUAVA', 'apple'}
                           #EVERYTIME WHEN YOU WILL RUN IT, TWO DIFFERENT ITEMS WILL APPEAR.
"""

 #IV.CLEAR() METHOD: IT EMPTIES THE SET.
"""
thisset={"apple","banana","GUAVA"}
thisset.clear()
print(thisset)            #set()
"""

 #V.DEL KEYWORD: DELETE THE SET COMPLETELY.
"""
thisset={"apple","banana","GUAVA"}
del thisset
print(thisset)           #NameError: name 'thisset' is not defined
                         #BCOZ IT'S DELETED COMPLETELY
"""


        #COPY() METHOD: EAISLY YOU CAN MAKE A COPY OF SET.
"""
thisset={"apple","banana","GUAVA"}
s1=thisset.copy()
print(s1)                #{'GUAVA', 'banana', 'apple'}
"""



         #UNION & INTERSECTION

 #I.UNION: FOR UNION OF SET, A SYMBOL IS USED "|", CALLED PIPE or "OR".
"""
s1={1,2,3,4,5}
s2={3,4,5,6,7,8,9,10}
union=s1 | s2
print(union)             #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

s3={"apple","banana","GUAVA"}
s4={"cherry","lichi","apple","GUAVA"}
union1=s3|s4
print(union1)            #{'apple', 'GUAVA', 'cherry', 'banana', 'lichi'}
"""

 #II.INTERSECTION: FOR INTERSECTION OF SET, A SYMBOL IS USED "&", "AND".
"""
s1={1,2,3,4,5}
s2={3,4,5,6,7,8,9,10}
intersection=s1 & s2
print(intersection)             #{3, 4, 5}

s3={"apple","banana","GUAVA"}
s4={"cherry","lichi","apple","GUAVA"}
intersection1=s3&s4
print(intersection1)            #{'GUAVA', 'apple'}
"""



          #LENGTH OF A SET: FIND LENGTH OF A SET USING LEN() METHOD
"""
s4={"cherry","lichi","apple","GUAVA"}
print(len(s4))                  #4
"""



          #JOIN TWO SETS

          # BOTH UNION AND UPDATE METHODS, FOLLOWS UNIQUE RULE.
          # MEAN IF COMMON ITEM IS PRESENT, THEY WILL BE TAKEN SINGLE.
          
 #I.UNION() METHOD
"""
s1={1,2,3,4,5}
s2={6,7,8,9,10,'a','b'}
s3=s1.union(s2)
print(s3)                       #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'b', 'a'}
"""

 #II.UPDATE() METHOD: INSERT THE ITEM OF "ONE SET TO ANOTHER", MEAN UPDATE THE OLD SET DATA FROM THE NEW SET.
"""
s1={1,2,3,4,5}
s2={6,7,8,9,10,'a','b'}
s1.update(s2)
print(s1)                       #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'b', 'a'}
"""




         #THE SET CONSTRUCTOR

 #CONVERT A TUPLE INTO SET
"""
thisset=set(("apple","banana",1,2,3.4,5.6))
print(thisset)                  #{1, 2, 3.4, 5.6, 'apple', 'banana'}
"""
#CONVERT A LIST INTO SET

thisset=set(["apple","banana",1,2,3.4,5.6])
print(thisset)                  #{1, 2, 3.4, 'banana', 5.6, 'apple'}















































































































