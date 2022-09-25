                        #PYTHON VARIOUS FUNCTIONS WITH EXERCISES

         # 1.ENUMERATOR FUNCTION()
#WE USE ENUMERATE FUNCTION WITH FOR LOOP, TO TRACK POSITION OF OUR ITEM IN ITERABLE.
#GENERALLY WITH FOR LOOP WE TRACK THE ITEMS, NOT THEIR POSITIONS.

#HOW WE CAN DO IT WITHOUT ENUMERATE fn.
#i.e.
"""         
l=['abs','cde','qwert','zxcv','ghjkl']
pos=0
for i in l:                              
    print(f"AT {pos}th postion: {i}")
    pos+=1                                   #AT 0th postion: abs
                                             #AT 1th postion: cde
                                             #AT 2th postion: qwert
                                             #AT 3th postion: zxcv
                                             #AT 4th postion: ghjkl
"""

#WITH ENUMERATE fn.
"""
l=['abs','cde','qwert','zxcv','ghjkl']

for pos,i in enumerate(l):
    print(f"AT {pos}th postion: {i}")        #AT 0th postion: abs
                                             #AT 1th postion: cde
                                             #AT 2th postion: qwert
                                             #AT 3th postion: zxcv
                                             #AT 4th postion: ghjkl
"""

              #EXERCISE-I
#DEFINE A FUNCTION THAT TAKES TWO ARGUMENTS.
#1.A LIST THAT CONTAINS STRINGS.
#2.STRING, WHICH POSITION IS TO BE FIND OUT.
#AND THIS fn WILL RETURN THE INDEX OF STRING YOU WILL PASS.
#IF NOT THEN IT RETURN  -1.

def find_index(l):
    print(l)
    s=input(print("\nWhich one's string you wanna know, Enter:\n"))
    for pos,dzire_str in enumerate(l):
        if dzire_str==s:
            return pos

lst=['abs','cde','qwert','zxcv','ghjkl']

print(find_index(lst))                      #if s==zxcv, o/p=3
                                            #Similarly others can be find out.



        #  2.MAP() FUNCTION




 








                                      































    
