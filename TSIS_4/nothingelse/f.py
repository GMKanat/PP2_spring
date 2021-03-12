import re

pattern = r'^(7|8|9)\d{9}$'
x = int(input())
for i in range(x):
    k = re.search(pattern, input())
    if k:
        print("YES")
    else:
        print("NO")
