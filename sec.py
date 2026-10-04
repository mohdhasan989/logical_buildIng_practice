"""Find the Second Largest Number Given a list of integers, find the
    second largest number without using sort(). Example: Input: [10, 45,
    23, 45, 12] Output: 23 Follow-up: Handle duplicates. O(n)."""

num= [10, 45, 23, 45, 12]
def seclnum(num):
    lar = num[0]
    Slar = num[0]
    for n in num:
        if n > lar:
            Slar=lar
            lar=n
        elif n > Slar and n!=lar:
            Slar=n
    return Slar
print(seclnum(num))
