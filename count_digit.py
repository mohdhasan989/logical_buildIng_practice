def count_digi(n):
    count=0
    if n==0:
        return 1
    while n:
        count+=1
        n=n//10
    return count
print(count_digi(12345678098765432))