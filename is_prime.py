def is_prime(a):
    if a<=1:
        print("not prime")
        return 
    for i in range(2,a):
        if a%i==0:
            print("not prime")
            return 

    print("prime")
is_prime(67)
