a=25
b=125
def lcm(a,b):
    i=max(a,b)

    while True:
        if i % a == 0 and i % b== 0 :
            return i
        i += 1
print(lcm(a,b))
