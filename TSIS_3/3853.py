# b =input()#эта строка необязательна
a = input().split()
k = int(input())
k = k%len(a)
if k<0:
    k = abs(k)
    print(*a[k:],end =' ')
    print(*a[0:k])
 
else:
    print(*a[-k:],end =' ')
    print(*a[0:-k])
    exit()