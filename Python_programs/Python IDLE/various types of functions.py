# 1.MAX AND MIN FUNCTION: RETURNS THE MAXIMUM AND MINIMUM VALUES

a=[12,34,67,2,5,9]
print(max(a))   #67
print(min(a))   #2

b=['banana','he','i']
print(max(b))   #banana
print(min(b))   #i

#ex. I.DEFINE A FUNCTION WHICH TAKES INPUT AS A LIST, AND RETURN US DIFFERENCE OF GREATEST-SMALLEST NO ISNSIDE THE LIST
a=[34,45,2,67,98,5,68,23,12]
def diff(l):
    return max(l)-min(l)
print(diff(a))                      #o/p '96' i.e. 98-2


# 2.
