def reverse(n):
        res=0
        while n>0:
            a=n%10
            res=res*10+a
            n//=10
        return res
print(reverse(123987654))