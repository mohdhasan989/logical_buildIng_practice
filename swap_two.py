#Swap two numbers without using a third variable.
a=40
b=30
c=70
d=55
def swap(a,b):
    a , b = b , a
    return a, b

a,b =swap(  c,  a)
print ('c:', a, "a:" ,b)