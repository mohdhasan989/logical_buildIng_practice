#9. Count the frequency of digits in a number.
num=[1,3,2,4,4,5,5,5,4]
def freq_count(num):
    digit=set(num)
    cont={}
    for digit in num:
        if digit in cont:
            cont[digit] +=1
        else:
            cont[digit]=1
    return cont
print(freq_count(num))
'''num=[1,3,2,4,4,5,5,5,7,8,9,9,9,9]
digit=set(num)
print(digit)'''
