def is_pilindorm(n):
    rev=0
    orginal=n
    if n==0:
        return 1
    while n>0:
        a=n%10
        rev=rev*10+a
        n//=10
    if rev==orginal:
        return "palindorm"
    else:
        return "Not Palindrome"
print(is_pilindorm(12221))

    

