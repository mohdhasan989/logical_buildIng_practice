#reverse str
string="banana"
def rev_str(s):
    res="" 
    for i in s:
        res = i + res
    return res
print(rev_str(string))

