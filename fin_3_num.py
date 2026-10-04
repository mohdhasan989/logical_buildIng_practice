a = 10
b = 25
c = 40

def large_third(a,b,c):
    if a > b and a >c:
        return a
    elif b>c:
        return b
    else: 
        return c
print(large_third(a, b, c))

    