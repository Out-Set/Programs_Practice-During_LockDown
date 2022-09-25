                             #PYTHON CLASSES/OBCECTS WITH EXERCISES

#WE CREATE CLASSES SO THAT WE CAN MAKE OUR OWN OBJECTS.
#PYTHON IS AN OBJECT ORIENTED PROGRAMMING LANGUAGE.
#ALMOST EVERYTHING IN PYHTON IS AN OBJECT, WITH IT'S PROPERTIES AND METHODS.
#A CLASS IS LIKE AN OBJECT CONSTRUCTOR, OR A "BLUEPRINT" FOR CREATING OBJECTS.
#IT'S JUST LIKE MAKING AN STRUCTURE IN "C" LANGUAGE.


                       #CREATE AN 'class'
#TO CREATE AN OBJECT USE THE KEYWORD "class".
class MyClass:
    x=5
                    
                       #CREATE AN 'object'    
#NOW WE CAN USE THE "class" NAMED "MyClass" TO CREATE OBJECTS.
p1=MyClass()
print(p1.x)                               #5



                       #THE "__init__()" FUNCTION

#THE EXAMPLES ABOVE ARE CLASSES AND OBJECTS IN THEIR SIMPLEST FORM, ARE NOT REALLY USEFUL IN REAL LIFE APPLICATIONS.
#TO UNDERSTAND THE MEANING OF CLASSES, WE HAVE TO UNDERSTAND THE BUILT-IN __init__() function.
#ALL CLASSES HAVE A FUNCTION CALLED __init__ ,WHICH IS ALWAYS EXECUTED WHEN THE CLASS IS BEING INITIATED.
#USE THE __init__ FUNCTION TO ASSIGN VALUES TO OBJECT PROPERTIES, OR OTHER OPERATIONS THAT ARE NECESSARY TO DO WHEN THE OBJECT IS BEING CREATED.
#IT'S ALSO KNOWN AS "CONSTRUCTOR".

##IT'S A CONVENTION THAT THE FIRST LETTER OF THE CLASS SHOULD BE IN CAPITAL LETTER(i.e. Person,MyClass....) &
##INSIDE __init__ FUNCTION, FIRSTLY WE WRITE ONLY "self". ALTHOUGH THESE CONVENTIONS ARE NOT NECESSARY, YOU  MAY WRITE WHATEVER YOU WANT.

#i.e.
"""
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        
p1=Person('ankur','prajapati',18)
p2=Person('sawan','kumar',22)

print(p1.first_name)                      #ankur
print(p2.first_name)                      #sawan

print(p1.last_name)                       #prajapati
print(p2.last_name)                       #kumar

#TO PRINT ALL THE INFORMATION OF ANY OBJECT.
print(p1.__dict__)     #{'first_name': 'ankur', 'last_name': 'prajapati', 'age': 18}
print(p2.__dict__)     #{'first_name': 'sawan', 'last_name': 'kumar', 'age': 22}
"""

#NOTE: THE __init__() FUNCTION IS CALLED AUTOMATICALLY EVERY TIME THE CLASS IS BEING USED TO CREATE A NEW OBJECT.
#i.e.
"""
class Person:
    def __init__(self,first_name,last_name,age):
        print("__init method//constructor get called")
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        
p1=Person('ankur','prajapati',18)
p2=Person('sawan','kumar',22)

print(p1.first_name)                     
print(p2.first_name)                     
"""                                       #__init method//constructor get called
                                          #__init method//constructor get called
                                          #(it's being called two times, because of two objects)
                                          #ankur  
                                          #sawan

#WE CAN CHANGE THE INSTANCE VARIABLES NAMES from left side, IT'S NOT NECESSARY TO BE SAME BOTH SIDES.
#i.e.
"""
class Person:
    def __init__(self,first_name,last_name,age):
        print("__init method//constructor get called")
        self.person_first_name=first_name
        self.the_last_name=last_name
        self.age=age
        
p1=Person('ankur','prajapati',18)

print(p1.person_first_name)                     
print(p1.the_last_name) 
"""                                        #__init method//constructor get called
                                           #ankur
                                           #prajapati

#"self" IS AN OBJECT(i.e. p1,p2....) IN __init__() FUNCTION, IT'S NOT NECESSARY TO WRITE "self" AFTERALL.
#i.e.
"""
class Person:
    def __init__(man,first_name,last_name,age):
        print("__init method//constructor get called")
        man.person_first_name=first_name
        man.the_last_name=last_name
        man.age=age
        
p1=Person('ankur','prajapati',18)

print(p1.person_first_name)                     
print(p1.the_last_name) 
"""                                        #__init method//constructor get called
                                           #ankur
                                           #prajapati

           #Exercise-I
#CREATE A LAPTOP CLASS WITH ATTRIBUTES, BRAND NAME, MODEL NAME, PRICE.
#CREATE TWO OBJECTS/INSTANCE OF YOUR LAPTOP CLASS.
"""
class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.b_name=brand_name
        self.m_name=model_name
        self.p=price

l1=Laptop('Lenovo','81DE',42600)
l2=Laptop('Dell','XP1200',40000)

print(l1.b_name)                            #Lenovo
print(l2.p)                                 #40000  
print(l1.m_name)                            #81DE
print(l2.b_name)                            #Dell
"""




                        #OOP's-INSTANCE METHOD

#INSTANCE & OBJECTS ARE SAME, 
#i.e.
l=[12,34,56,67,89,45]
#HERE "l" IS AN INSTANCE/OBJECTS OF LIST CLASS.
#NOW WITH THIS INSTANCE(l), WE CAN PERFORM MANY OPERATIONS(LIKE POP()/APPEND() METHODS...etc)

#SO HERE IN INSTANCE METHOD, WE WILL LEARN HOW TO CREATE A METHOD, THAT WILL BE PERFORMED.
#i.e.
"""
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        
   #ANY METHOD INSIDE CLASS, IS A FUCTION. SO IT WILL BE DEFINED AS A FUNCTION.        
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def is_age_above_18(self):
        return self.age>18    
        
p1=Person('ankur','prajapati',18)

#NOW WE HAVE TO DEFINE A METHOD THAT WILL GIVES US FULL NAME.
print(p1.full_name())                         #ankur prajapati
print(p1.is_age_above_18())                   #False

#BUT IN ACTUAL: "p1.full_name()=Person.full_name(p1)" IS HAPPENING IN BACKGROUND, YOU CAN SEE BELOW IT...

#TO AVODING IT(Person.full_name(p1)), WE HAVE WRITTEN "self" ABOVE IN THE FUNCTION "full_name(self)".....
print(Person.full_name(p1))                   #ankur prajapati
"""

##NOTE: 1.THE "self" PARAMETER IS A REFERENCE TO THE CURRENT INSTANCE OF THE CLASS, AND IS USED TO ACCESS VARIABLES THAT BELONG TO THE CLASS.
##      2.IT DOES NOT HAVE TO BE NAMED "self", YOU CAN CALL IT WHENEVER YOU LIKE,BUT IT HAS TO BE THE FIRST PARAMETER OF ANY FUNCTION IN THE CLASS.

#TO UNDERSTAND IT IN A BETTER WAY, SUPPOSE WE HAVE A LIST...& WE WANNA CLEAR IT.
l=[12,34,56,67,89,45]
#WE WRITES...
l.clear()
print(l)                                      #[]
#IT CAN BE DONE ALSO IN THE FOLLOWING MANNER....
list.clear(l)
print(l)                                      #[]

#NOW YOU THINK, IF WE HAVE TO APPEND SOMETHING, THEN WHAT...IT WILL WE DONE AS.....
#COMMONLY WE WRITES...
l.append(10)   #ACTUALLY IN BACKGROUND THIS(list.append(l,10)) IS GOING ON.
print(l)                                      #[10]
##IT CAN BE DONE AS.....
list.append(l,10)
print(l)                                      #[10, 10]
#YOU SEE WHENEVER YOU WANNA APPEND SOMETHING, EVERY TIME YOU HAVE TO TYPE "l" INSIDE APPEND.
#THAT'S WHY WE SIMPLY USE "l.append(10)" IT.

#DUE TO THIS REASON, WE HAVE WRITTEN "self" IN ABOVE FUNCTION.

#IN THE SAME WAY ABOVE OPERATIONS WERE DONE.


            #Exercise-II
#CREATE A PROGRAM FOR LAPTOP, THAT CALCULATE THE ACTUAL PRICE AGAINST THE OFF PRICE.
"""
class Laptop:
    def __init__(self,brand_name,price):
        self.brand_name=brand_name
        self.price=price

    def off_price(self,num):
        off_price=(num/100)*self.price
        return self.price-off_price
         
l1=Laptop('Lenovo',42600)
l2=Laptop('Dell',50000)
l3=Laptop('HP',25600)

print("Which one laptop you wanna buy:\n 1.'Lenovo' actual price-42600 you get 20% discount\n 2.'Dell' actual price-50000 you get 25% discount\n 3.'HP' actual price-25600 you get 32% discount")
n=int(input("Please input your choice 1, 2, or 3 to get the actual price\n"))

if n==1:
    print(l1.off_price(20))
if n==2:
    print(l2.off_price(25))
if n==3:
    print(l3.off_price(32))

#IF INPUT=1                                    #34080.0
#IF INPIT=2                                    #37500.0
#IF INPUT=3                                    #17408.0
"""





                        #OOP's-CLASS VARIABLE

#WE SAW THAT INSTANCE VARIABLES WERE UNIC.
#i.e. IN ABOVE EXERCISE l1,l2,l3 EVERY OBJECTS HAVE DIFFERENT VARIABLE.

#BUT IN CLASS VARIABLES VALUES ARE SHARED B//W ONE ANOTHER.
#i.e. CERATE A CIRCLE-'class' & DEFINE METHODS THAT CAN CALCUALTE AREA & CIRCUMFERENCE OF THE CIRCLE.
"""
class Circle:
    def __init__(self,radius,pi):
        self.radius=radius
        self.pi=pi
    def circumference(self):
        return 2*self.pi*self.radius
    def area(self):
        return self.pi*(self.radius)**2

c1=Circle(23,3.14)
c2=Circle(20,3.14)

print(c1.area())                              #1661.0600000000002
print(c2.circumference())                     #125.60000000000001
"""

     #NOW HERE IS TWO PROBLEMS..........
#THE VALUE OF PI IS SAME FOR EVERY OBJECT.
#1.EVERY TIME YOU HAVE TO WRITE "3.14", WHENEVER YOU WILL MAKE A NEW OBJECT.
#2.IT WILL CONSUME MEMORY FOR EVERY OBJECT OF THIS VARIABLE(3.14), BECAUSE FOR EVERY OBJECT THIS VARIABLE(3.14) WILL BE CREATED IN MEMORY EVERY TIME, SO WASTAGE OF MEMORY.

#WE CAN RESOLVE IT ......
"""
class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def circumference(self):
        return 2*Circle.pi*self.radius
    def area(self):
        return Circle.pi*(self.radius)**2
    
c1=Circle(23)
c2=Circle(20)

print(c1.area())                              #1661.0600000000002
print(c2.circumference())                     #125.60000000000001
"""                                           #SAME OUTPUT, AS OF PREVIOUS


            #EXERCISE-III
#YOU HAVE STARTED A SELL,THAT ON EVERY LAPTOP YOU ARE GIVING 10% DISCOUNT.
#CREATE A PROGRAM FOR LAPTOP, THAT CALCULATE THE ACTUAL PRICE AGAINST THE OFF PRICE.
"""
class Laptop:
    discount=10
    def __init__(self,brand_name,price):
        self.brand_name=brand_name
        self.price=price

    def off_price(self):
        off_price=(Laptop.discount/100)*self.price
        return self.price-off_price
         
l1=Laptop('Lenovo',42600)
l2=Laptop('Dell',50000)
l3=Laptop('HP',25600)

print("Which one laptop you wanna buy:\n 1.'Lenovo' actual price-42600 \n 2.'Dell' actual price-50000 \n 3.'HP' actual price-25600 \n on every laptop you get 10% discount")
n=int(input("Please input your choice 1, 2, or 3 to get the actual price\n"))

if n==1:
    print(l1.off_price())
if n==2:
    print(l2.off_price())
if n==3:
    print(l3.off_price())

#IF INPUT=1                                    #38340.0
#IF INPIT=2                                    #45000.0
#IF INPUT=3                                    #23040.0
"""

             #EXERCISE-IV
#SUPPOSE YOUR SELL HAS BEEN ENDED, NOW EVERYTHING ON THE ACTUAL PRICE.
"""
class Laptop:
    discount=10
    def __init__(self,brand_name,price):
        self.brand_name=brand_name
        self.price=price

    def off_price(self):
        off_price=(Laptop.discount/100)*self.price
        return self.price-off_price
    
#SIMPLY WRITE A LINE...IF DISCOUNT SELL IS NO MORE.
Laptop.discount=0     #FROM HERE YOU CAN ALSO MAKE CHANGES IN DISCOUNTS.
l1=Laptop('Lenovo',42600)
l2=Laptop('Dell',50000)
l3=Laptop('HP',25600)

print("Which one laptop you wanna buy:\n 1.'Lenovo' actual price-42600 \n 2.'Dell' actual price-50000 \n 3.'HP' actual price-25600")
n=int(input("Please input your choice 1, 2, or 3 to get the price of laptops\n"))

if n==1:
    print(l1.off_price())
if n==2:
    print(l2.off_price())
if n==3:
    print(l3.off_price())

#IF INPUT=1                                    #42600.0
#IF INPIT=2                                    #50000.0
#IF INPUT=3                                    #25600.0
"""

##SUPPOSE WE HAVE SOME LAPTOPS THAT IS ON OTHER DISCOUNTS, AND ALSO WE WANNA USE 'CLASS VARIABLE', THAT IS NOT POSSIBLE IN ABOVE PROGRAM......THEN WHAT....
"""   
class Laptop:
    discount=10
    def __init__(self,brand_name,price):
        self.brand_name=brand_name
        self.price=price

    def off_price(self):
        off_price=(self.discount/100)*self.price
        #Laptop.discount is EXCHANGED TO "self.discount"
        return self.price-off_price
    
l1=Laptop('Lenovo',42600)
l2=Laptop('Dell',50000)
l3=Laptop('HP',25600)
l4=Laptop('Acer',30000)
l5=Laptop('Asus',20000)
l6=Laptop('MacBOOK',120000)
l7=Laptop('Samsung',75000)

#'l1,l2 and l3' ARE AT THEIR INITIAL DISCOUNT ON 10% YET, BUT WE HAVE OTHERS BELOW.....
#SUPPOSE LAPTOP 'l4 & l5 ' HAVE 20%,'l6' HAVE 50% AND 'l7' HAVE 0% DISCOUNT RESPECTIVELLY.....
print("ACTUAL PRICE OF LAPTOPS:\n1.Lenovo-42600\n2.Dell-50000\n3.HP-25600\n4.Acer-30000\n5.Asus-20000\n6.MacBOOK-120000\n7.Samsung-75000\n")
print("Which one laptop you wanna buy:\nA.Lenovo, Dell & HP on 10%\nB.Acer & Asus on 20% and\nC.Apple MacBOOK ON 50% discount\nD.Samsung on 0% discount\n")
n=int(input("Please input your choice\n1 for Lenovo\n2 for Dell\n3 for HP\n4 for Acer\n5 for Asus\n6 for Apple MacBOOK\n7 for Saamsung: To get the actual price\n"))

if n==1:
    print(l1.off_price())
if n==2:    
    print(l2.off_price())
if n==3:
    print(l3.off_price())
if n==4:
    l4.discount=20
    print(l4.off_price())
if n==5:
    l5.discount=20
    print(l5.off_price())
if n==6:
    l6.discount=50
    print(l6.off_price())
if n==7:
    l7.discount=0
    print(l7.off_price())

#IF N=1                                       #38340.0
#IF N=2                                       #45000.0 
#IF N=3                                       #23040.0 
#IF N=4                                       #24000.0 
#IF N=5                                       #16000.0 
#IF N=6                                       #60000.0       
#IF N=7                                       #75000.0
"""

            #EXERCISE-V
#DEFINE A CLASS,AND COUNT HOW MANY INSTANCES/OBJECTS HAVE BEEN CREATED OF THIS CLASS.
"""
class Group:
    count_instance=0
    def __init__(self,name,age,department):
        Group.count_instance+=1
        self.name=name
        self.age=age
        self.dep=department

p1=Group('Sawan',22,'CSE')
p1=Group('Prateek',20,'CSE')
p1=Group('Mohan',21,'CSE')

print(Group.count_instance)                   #3
"""




                        #OOP's-Class Methods

    To read it firstly complete decorator chapter













































