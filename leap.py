#Check whether a year is a leap year.

def check_leap(year):
    if ((year % 400 ==0) or (year % 4 == 0 and year % 100 != 0)):
        print("leap year")
    else :
        print( "not_leap")

check_leap(2024)