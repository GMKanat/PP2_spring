def h(n, x, y):
    if n >0:
        tmp = 6 - x-y
        h(n-1, x, tmp)
        print(x, y)
        h(n-1, tmp, y)
n = int(input())
h(n, 1, 3)