#Check whether a string is a palindrome
def str_palindrome(str):
    rev=str[::-1]
    if str==rev:
        print("palindrome")
    else:
        print("na")
    return rev
str="appa"
print(str_palindrome(str))

'''A="apple"
B=A[::-1]
print(B)'''

