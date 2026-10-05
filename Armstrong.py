#Check whether a number is an Armstrong number.

def armstrong(num):
    count=len(str(num))
    value=0
    for i in str(num):
        x= int(i) ** count
        value=x+value
    if value==num:
        return "armstrong" 
    else:
        return "not armstrong"   
#num=153
print(armstrong(153))

