#Find the sum of digits of a number.
num=(987654321)
def sum_digi(num):
    num=str(num)
    sum=0
    for i in num:
        sum=sum+int(i)
    return sum

print(sum_digi(num))