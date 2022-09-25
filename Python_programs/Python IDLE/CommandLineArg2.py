from sys import argv
y=0
s=0
for i in argv: 
   if y==0:
      y=1
   else:
      s=s+int(i)
print("Sum is: ",s)