import math
a=input()
b=input()

y=[]
z=[]
for i in range(len(a)):
    if a[i] == b:
        y.append(i)
mn=1000000
for i in range(len(a)):
    for j in y:
        ans = abs(i-j)
        if ans < mn:
            mn = ans
    z.append(mn)
    mn=1000000
print(*z)