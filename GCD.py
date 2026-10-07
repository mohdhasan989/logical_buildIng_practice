#Find the GCD of two numbers

a=19
b=18

def find_gcd(a,b):
    factor=[]
    for i in range(1,a+1):
        if a % i == 0:
            factor.append(i)
    common=[]
    for i in factor:
        if b % i ==0:
            common.append(i)
    return max(common)
print("GCD:",find_gcd(a,b))
