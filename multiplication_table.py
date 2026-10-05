#Print the multiplication table of a number.

def multipication(n):
    for i in range(1,11):
        table=i * n
        print(table)
        #i+=1
        
n=17
multipication(n)