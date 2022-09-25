
def palindrome(a):
    #return (a==(a[::-1]))  OR
    if a==a[::-1]:
        return "IT IS PALINDROME"
    return "it is not PALINDROMRE"
b=input("enter a word")
print(palindrome(b))

