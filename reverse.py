num=[9,1,2,3,4,5,6,7]


def reverse(num):
    i= 0
    j= len(num)-1
    while i < j:
        num[i], num[j]= num[j],num[i]
        i +=1
        j -=1
    return num
print(reverse(num))
       