def prime(a,b):
    for i in range(a,b):
        if i % 2== 0:
            pass
        else:
            print(i)
        i=i+1
        prime(i,b)
        return 0
    
prime(1,100)

