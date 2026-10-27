#23. Count vowels in a string.
def cont_vow(word):
    vowels=["a","e","i","o","u"]
    count=0
    for i in word.lower():
        if i in vowels:
            count+=1
    return count
print(cont_vow("HASannn"))
