                           #SET COMPREHENSION WITH EXAMPLES

        #WE CAN CREATE OUR SETS IN JUST ONE LINE, LIKE LIST & DICTIONARY COMPREHENSION.

#TO PRINT THE SQUARE OF N NUMBERS.
myset={i**2 for i in range(1,6)}
print(myset)                             #{1, 4, 9, 16, 25}


#TO PRINT THE FIRST CHAR OF A NAME.
names={"sawan","ankur","divya"}
name={i[0] for i in names}
print(name)                              #{'s', 'd', 'a'}
