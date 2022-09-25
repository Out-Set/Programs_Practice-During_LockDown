                        #DICTIONARY COMPREHENSION WITH EXAMPLES

       #WE CAN CRETAE A DICTIONARY JUST IN ONE LINE, IT'S JUST LIKE LIST COMPREHENSION, BUT IT CONTAIN "KEY AND VALUE".

 #TO PRINT THE SQUARE OF N NUMBERS
#I. BY SIMPLE METHOD









#II.BY DICTIONARY COMPREHENSION.
"""
square={i:i**2 for i in range(1,6)}
print(square)                         #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

square={f"square of {i}":i**2 for i in range(1,6)}
print(square)                         #{'square of 1': 1, 'square of 2': 4, 'square of 3': 9, 'square of 4': 16, 'square of 5': 25}

square={f"square of {i}":i**2 for i in range(1,6)}
for i,j in square.items():
    print(f"{i}:{j}")                 #square of 1:1
                                      #square of 2:4
                                      #square of 3:9
                                      #square of 4:16
                                      #square of 5:25
"""

 #TO COUNT THE NUMBER OF CHAR IN A STRING.
"""
string="sawan"
d={char:string.count(char) for char in string}
print(d)                              #{'s': 1, 'a': 2, 'w': 1, 'n': 1}
"""


             #DICTIONARY COMPREHENSION WITH "IF STATEMENT".

#FILTER ODD & EVEN NUMBER.
"""
dict={i:('even' if i%2==0 else 'odd') for i in range(1,6)}
print(dict)                           #{1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}
"""
