num = [1,1,1,2,2,2,2,2,3,5,5,5,9,9,9]
def feq(num):
    frequency={}
    for i in num:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
    print(frequency)
feq(num)