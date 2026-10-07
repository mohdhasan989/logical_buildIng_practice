#Calculate the power of a number without using `**`.
base = 5
exponent = 2

def power_cal(base,exponent):
    result = 1

    for i in range(exponent):
        result = result * base
    print(result)

power_cal(base,exponent)