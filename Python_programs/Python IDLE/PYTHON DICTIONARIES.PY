                          #PYTHON DICTIONARIES & EXERCISE ON IT.

#PYTHON DICTIONARIES IS A COLLECTION WHICH IS UNORDERED,CHANGEABLE(MUTABLE) AND INDEXED DATA TYPE IN PYTHON.
#WE USE PYTHON DICTIONARIES BECAUSE "LIMITATIONS OF LISTS", LIST ARE NOT ENOUGH TO REPRESENT REAL DATA.

           #CERATING A PYTHON DICTIONARY: PYTHON DICTIONARIES ARE WRITTEN WITH CURLY BRACKETS, AND THEY HAVE "KEY AND VALUE"...{key : value}

# I.SIMPLE METHOD
"""
thisdict={'name':'sawan','age':23,'college':'KNGD'}
print(thisdict)                             #{'name': 'sawan', 'age': 23, 'college': 'KNGD'}
"""
# II.THE DICT() CONSTRUCTER
"""
a=dict(name='sawan',age=23,college='KNGD')
print(a)                                    #{'name': 'sawan', 'age': 23, 'college': 'KNGD'}
"""


# III.USING "fromkeys() METHOD": RETURN A DICTIONARY WITH THE "SPECIFIED KEYS AND VALUES".
"""
d=dict.fromkeys(['name','age','hobbies'],'unknown')
print(d)                                    #{'name': 'unknown', 'age': 'unknown', 'hobbies': 'unknown'}
"""
     #YOU MAY AVOID THE LIST, INSIDE fromkeys().....AND CAN USE THE TUPLE....
"""
d=dict.fromkeys(('name','age','hobbies'),'unknown')
print(d)                                    #{'name': 'unknown', 'age': 'unknown', 'hobbies': 'unknown'}
"""
     #YOU MAY AVOID THE LIST & TUPLE, INSIDE fromkeys().....AND CAN USE THE STRINGS....
"""    
d=dict.fromkeys("ABC",'unknown')
print(d)                                    #{'A': 'unknown', 'B': 'unknown', 'C': 'unknown'}
"""
     #YOU MAY USE RANGE FUNCTION INSTEAD OF THESE ALSO,INSIDE fromkeys()....
"""     
d=dict.fromkeys(range(1,6),'unknown')
print(d)                                    #{1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown'}
"""
 #SOME EXAMPLES....
"""
print(dict.fromkeys(['name'],['sawan','mohan','ankur']))    #{'name': ['sawan', 'mohan', 'ankur']}
print(dict.fromkeys(['name'],('sawan','mohan','ankur')))    #{'name': ('sawan', 'mohan', 'ankur')}
"""  



           #ACCESSING ITEMS INSIDE DICTIONARY: we can't access it through "SLICING" method,because it's unordered & unindexed.

# I.SIMPLE METHOD
"""
thisdict={'name':'sawan','age':23,'college':'KNGD'}
print(thisdict['name'])                     #sawan
print(thisdict['age'])                      #23
"""

## II.GET() METHOD: GIVES THE SAME RESULT...IT RETURNES "NONE" IF THE KEY IS NOT PRESENT INSIDE DICTIONARY, BUT DOSEN'T RAISE AN ERROR.
"""
thisdict={'name':'sawan','age':23,'college':'KNGD'}
print(thisdict.get('name'))                 #sawan
print(thisdict.get('age'))                  #23
print(thisdict.get('hobby'))                #"None"
"""



           #DICTIONARIES CAN STORE ANYTHING: NUMBERS, STRINGS, LIST AS WELL AS DICTIONARIES.
"""
thisdict={
    'name':'sawan',
    'age':24,
    'fav_movie':['3_idiots','super_30'],
    'fav_book':['grand_unified_theory','theory_of_relativity']
    }
print(thisdict)
print(thisdict['fav_movie'])                 #['3_idiots', 'super_30']
print(thisdict['age'])                       #24
"""



           #"ADD DATA" TO EMPTY DICTIONARY OR "CHANGE VALUES" IN DICTIONARIES.
"""
sawan={}
sawan['name']='sawan prajapati'
sawan['age']=23
sawan['fav_mov']=['3_idiots','super_30']
print(sawan)                                  #{'name': 'sawan prajapati', 'age': 23, 'fav_mov': ['3_idiots', 'super_30']}


thisdict={
    'name':'sawan',
    'age':24,
    'fav_movie':['3_idiots','super_30'],
    'fav_book':['grand_unified_theory','theory_of_relativity']
    }
thisdict['name']='ankur prajapati'
thisdict['age']=19
print(thisdict)                                #{'name': 'ankur prajapati', 'age': 19, 'fav_movie': ['3_idiots', 'super_30'],
                                               #                  'fav_book': ['grand_unified_theory', 'theory_of_relativity']}
"""



           #CHECK IF KEY/VALUES EXISTS IN DICTIONARY: KEYS CAN BE DIRECTLY CHECKED BUT, FOR VALUES WE USE "VALUE() METHOD".

  #FOR keys: CHECK WHETHER THIS KEY IS PRESENT OR NOT.
"""
thisdict={
    'name':'sawan',
    'age':24,
    'fav_movie':['3_idiots','super_30'],
    'fav_book':['grand_unified_theory','theory_of_relativity']
    }
if 'name' in thisdict:
    print(f"present and name is: {thisdict['name']}")              #present and name is: sawan
else:
    print("not present")
    
 #GET() METHOD: "IT CHECKS ONLY KEYS, DON'T CHECK VALUES"
 
if thisdict.get('name'):
    print(f"present and is: {thisdict['name']}")                   #present and is: sawan
else:
    print("not present")
"""

  #FOR values: CHECK WHETHER THIS VALUE IS PRESENT OR NOT.
"""
thisdict={
    'name':'sawan',
    'age':24,
    'fav_movie':['3_idiots','super_30'],
    'fav_book':['grand_unified_theory','theory_of_relativity']
    }

  #VALUES() METHOD

if 'sawan' in thisdict.values():
    print("present")                     #present
else:
    print("not present")

if ['3_idiots','super_30'] in thisdict.values():    #FOR LISTS
    print("present")                     #present
else:
    print("not present")
"""



                #LOOP THROUGH A DICTIONARY

  #PRINT ALL THE KEYS NAMES ONE BY ONE.
"""
thisdict={
    'name':'sawan',
    'age':24,
    'fav_movie':['3_idiots','super_30'],
    'fav_book':['grand_unified_theory','theory_of_relativity']
    }
for x in thisdict:
    print(x)                           #name
                                       #age
                                       #fav_movie
                                       #fav_book
"""                                       

  #PRINT ALL THE VALUES NAMES ONE BY ONE: USING "values() FUNCTION"
"""
thisdict={
    'name':'sawan',
    'age':24,
    'fav_movie':['3_idiots','super_30'],
    'fav_book':['grand_unified_theory','theory_of_relativity']
    }
for x in thisdict.values():
    print(x)                           #sawan
                                       #24
                                       #['3_idiots', 'super_30']
        #OR                            #['grand_unified_theory', 'theory_of_relativity']

for x in thisdict:
    print(thisdict[x])                 #sawan
                                       #24
                                       #['3_idiots', 'super_30']
                                       #['grand_unified_theory', 'theory_of_relativity']
"""

  #PRINT ALL THE KEYS AND VALUSE NAMES BOTH: USING "items() FUNCTION"
"""
thisdict={
    'name':'sawan',
    'age':24,
    'fav_movie':['3_idiots','super_30'],
    'fav_book':['grand_unified_theory','theory_of_relativity']
    }
for x in thisdict.items():
    print(x)                           #('name', 'sawan')
                                       #('age', 24)
                                       #('fav_movie', ['3_idiots', 'super_30'])
                                       #('fav_book', ['grand_unified_theory', 'theory_of_relativity'])

for x,y in thisdict.items():   #PROFIT OF USING items() FUNCTION: WE CAN DEFINE KEYS AND VALUES SEPERATELY.
    print(f"key: {x} and value: {y}")  #key: name and value: sawan
                                       #key: age and value: 24
                                       #key: fav_movie and value: ['3_idiots', 'super_30']
                                       #key: fav_book and value: ['grand_unified_theory', 'theory_of_relativity']
"""




             #ADDING & REMOVING ITEMS THROUGH A DICTIONARIES


         # 1.ADDING ITEMS: 
"""
thisdict={
    'name':'sawan',
    'age':24,
    'fav_movie':['3_idiots','super_30'],
    'fav_book':['grand_unified_theory','theory_of_relativity']
    }
thisdict['fav_song']='song1','song2'
print(thisdict)                         #{'name': 'sawan', 'age': 24, 'fav_movie': ['3_idiots', 'super_30'],
                                        #   'fav_book': ['grand_unified_theory', 'theory_of_relativity'],
                                        #        'fav_song': ('song1', 'song2')}
"""



         # 2.REMOVING ITEMS:

 #I.USING POP() METHOD: REMOVES THE SPECIFIED ITEMS OF A DICTIONARY, REQUIRES ONE ARGUMENT AT LEAST.
"""
thisdict={'name': 'sawan',
         'age': 24,
         'fav_movie': ['3_idiots', 'super_30'],
         'fav_book': ['grand_unified_theory', 'theory_of_relativity'],
         'fav_song': ('song1', 'song2')
         }
#thisdict.pop()
#print(thisdict)                         #TypeError: pop expected at least 1 arguments, got 0    REQUIRES ONE ARG. AT LEAST
#print(thisdict.pop('fav_book'))         THIS WILL PRINT WHAT ITEM IS GOING OT BE POPPOD.
#thisdict.pop('fav_book')
#print(thisdict)                         #NOW FAV_BOOK KEY AND VALUE, HAS BEEN REMOVED

          ##YOU CAN CHECK THE "CLASS" OF POPPES ITEM   
#popped_item=thisdict.pop('fav_book')
#print(type(popped_item))                  #<class 'list'>
print(type(thisdict.pop('fav_book')))      #<class 'list'>
"""

 #II.USING POPITEM() METHOD: REMOVES THE LAST INSERTED ITEM OF A DICTIONARY, BY DEFAULT, SO NEED NOT AN ARGUMENT.
"""
thisdict={'name': 'sawan',
         'age': 24,
         'fav_movie': ['3_idiots', 'super_30'],
         'fav_book': ['grand_unified_theory', 'theory_of_relativity'],
         'fav_song': ('song1', 'song2')
         } 
#print(thisdict.popitem())                #THIS WILL PRINT WHAT ITEM IS GOING OT BE POPPOD
thisdict.popitem()
print(thisdict)                           #LAST ITEM FAV_SONG WILL BE REMOVED
print(type(thisdict.popitem()))           #<class 'tuple'>
"""

 #III.USING DEL KEYWORD: REMOVES THE ITEMS WITH THE "SPECIFIED KEY NAME", ALSO CAN "DELETE THE DICTIONARY COMPLETELY".

  #TO REMOVE A SPECIFIED KEY
"""
thisdict={'name': 'sawan',
         'age': 24,
         'fav_movie': ['3_idiots', 'super_30'],
         'fav_book': ['grand_unified_theory', 'theory_of_relativity'],
         'fav_song': ('song1', 'song2')
         } 
del thisdict['name']
print(thisdict)                            #NAME KEY AND VALUE HAS BEEN REMOVED
"""

  #TO DELETE THE DICTIONARY COMPLETELY
"""
thisdict={'name': 'sawan',
         'age': 24,
         'fav_movie': ['3_idiots', 'super_30'],
         'fav_book': ['grand_unified_theory', 'theory_of_relativity'],
         'fav_song': ('song1', 'song2')
         }
del thisdict
print(thisdict)   #NameError: name 'thisdict' is not defined: because thisdict has been deleted completely
"""

 #IV.USING CLEAR() KEYWORD: IT "EMPTIES" THE DICTIONARY.
"""
thisdict={'name': 'sawan',
         'age': 24,
         'fav_movie': ['3_idiots', 'super_30'],
         'fav_book': ['grand_unified_theory', 'theory_of_relativity'],
         'fav_song': ('song1', 'song2')}
thisdict.clear()
print(thisdict)                             #{}:  IT HAS BEEN EMPTY
"""



           #COPY A DICTIONARY
 #I.COPY() METHOD
"""
thisdict={'name':'sawan','age':23,'college':'KNGD'}
d=thisdict.copy()    #THESE BOTH ARE DIFFERENT DICTIONARIES,MEAN THEY DON'T HAVE SAME LOCATION IN MEMORY.
print(d)                     #{'name': 'sawan', 'age': 23, 'college': 'KNGD'}
print(d==thisdict)           #True: BECAUSE THESE TWO DICTIONARY HAVE SAME ITEM.
print(d is thisdict)         #False: BECAUSE THESE TWO DICTIONARY "HAVEN'T SAME LOCATION IN MEMORY".

print(d.popitem())           #('college', 'KNGD'): we have popped out it...ONLY FROM D..     
print(d)                     #{'name': 'sawan', 'age': 23}: here it's popped out...but
print(thisdict)              #{'name': 'sawan', 'age': 23, 'college': 'KNGD'}: still it's showing here.....
                     #SO FROM THESE ALL VARIOUS SOLUTION SHOWS THAT "D AND THISDICT" ARE NOT EQUAL.
      
d=thisdict                   #THESE BOTH ARE SAME DICTIONARIES, MEAN THEY HAVE SAME LOCATION IN MEMORY.
print(d==thisdict)                          #True: BECAUSE THESE TWO DICTIONARY HAVE SAME ITEM.
print(d is thisdict)                        #True: BECAUSE THESE TWO DICTIONARY HAVE "SAME LOCATION IN MEMORY".

print(d.popitem())           #('college', 'KNGD'): we have popped out it...ONLY FROM D..     
print(d)                     #{'name': 'sawan', 'age': 23}: here it's popped out...AND
print(thisdict)              #{'name': 'sawan', 'age': 23}: still it's ALSO POPPED FROM HERE here.....
                     #SO FROM THESE ALL VARIOUS SOLUTION SHOWS THAT "D AND THISDICT" ARE EQUAL.
"""

#II.DICT() METHOD
"""
thisdict={'name':'sawan','age':23,'college':'KNGD'}
d=dict(thisdict)
print(d)                     #{'name': 'sawan', 'age': 23, 'college': 'KNGD'}
"""


           

           #UPDATE() METHOD: IT "UPDATE" OUR PREVIOUS DICTIONARY, WITH NEW ONE.
"""
dict1={'name': 'sawan',
         'age': 24,
         'fav_movie': ['3_idiots', 'super_30'],
         'fav_book': ['grand_unified_theory', 'theory_of_relativity'],
         'fav_song': ('song1', 'song2')
          }
dict2={
    'fav_game':'cricket',
    'hobby':'programming',
    }
dict1.update(dict2)
print(dict1)                   #DICT1 HAS BEEN UPDATED, WITH DICT2 DATA.
                                            # {'name': 'sawan', 'age': 24,
                                            #    'fav_movie': ['3_idiots', 'super_30'],
                                            #     'fav_book': ['grand_unified_theory', 'theory_of_relativity'],
                                            #     'fav_song': ('song1', 'song2'),
                                            #     'fav_game': 'cricket',
                                            #     'hobby': 'programming'}
"""

  #IF ANY KEY OF DICT1 ALSO IN DICT2 ex.IF "NAME KEY" IS ALSO GIVEN IN DICT2 THEN.....
"""
dict1={'name': 'sawan',
         'age': 24,
         'fav_movie': ['3_idiots', 'super_30'],
         'fav_book': ['grand_unified_theory', 'theory_of_relativity'],
         'fav_song': ('song1', 'song2')
          }
dict2={
    'name':'sawan prajapati',
    'fav_game':'cricket',
    'hobby':'programming',
    }
dict1.update(dict2)
print(dict1)                   #NAME JUST GOT UPDATED....FROM sawan TO sawan prajapati.....     
                                            # {'name': 'sawan prajapati', 'age': 24,
                                            #    'fav_movie': ['3_idiots', 'super_30'],
                                            #     'fav_book': ['grand_unified_theory', 'theory_of_relativity'],
                                            #     'fav_song': ('song1', 'song2'),
                                            #     'fav_game': 'cricket',
                                            #     'hobby': 'programming'}
"""

   #IF YOU LEAVES UPDATE() "PARENTHESIS EMPTY": THEN NO DATA BE UPDATED.                                           
"""   
dict1={'name': 'sawan',
         'age': 24,
         'fav_movie': ['3_idiots', 'super_30'],
         'fav_book': ['grand_unified_theory', 'theory_of_relativity'],
         'fav_song': ('song1', 'song2')
          }
dict2={
    'name':'sawan prajapati',
    'fav_game':'cricket',
    'hobby':'programming',
    }
dict1.update()
print(dict1)              #NO DATA HAS CHANGED FROM DICT1, IT'S STILL LIKE "PREVIOUS".
                               # {'name': 'sawan', 'age': 24,
                               #    'fav_movie': ['3_idiots', 'super_30'],
                               #     'fav_book': ['grand_unified_theory', 'theory_of_relativity'],
                               #     'fav_song': ('song1', 'song2')}
"""



            #MORE ABOUT GET() FUNCTION
"""
 #I.YOU CAN GET IN "RETURN ANYTHING", WHAT YOU WANT AT THE PLACE OF "None".
dict2={
    'name':'sawan prajapati',
    'fav_game':'cricket',
    'hobby':'programming',
    }
print(dict2.get('age'))                 #None  
print(dict2.get('age','Not found!'))    #Not found!
"""

            #NESTED DICTIONARIES: A DICTIONARY CAN ALSO CONTAIN MANY DICTIONARY, CALLED NESTED DICTIONARY.
"""
my_family={
    'mem1':{'name':'sawan','age':23},
    'mem2':{'name':'rohit','age':22},
    'mem3':{'name':'vijayant','age':24},
    'mem4':{'name':'roman','age':24},
    'mem5':{'name':'manmohan','age':21}
    }
print(my_family)        #{'mem1': {'name': 'sawan', 'age': 23},
                        #   'mem2': {'name': 'rohit', 'age': 22},
                        #   'mem3': {'name': 'vijayant', 'age': 24},
                        #   'mem4': {'name': 'roman', 'age': 24},
                        #   'mem5': {'name': 'manmohan', 'age': 21}}
"""


            #MORE ABOUT DICTIONARIES

# 1.IF WE HAVE MORE THAN ONE KEY VALUES pairs IN OUR DICTIONARY, THEN IT WILL "OVERWRITE TO THE "LAST" KEY VALUES"....
"""
dict1={'name':'sawan','age':24,'age':23}
print(dict1)                   #{'name': 'sawan', 'age': 23}
"""

















































                  











































    
    



































                                               



























