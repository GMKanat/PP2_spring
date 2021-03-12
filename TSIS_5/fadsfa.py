import re

pattern = r'^(1299|1[3-8]\d\d|19[0-1]]\d|192[0-2])\s(0[1-9]|1[0-2])\s(0[1-9][1-2]\d|3[0-1])$'

m = re.search(pattern, input())
print("YES" if m else "NO")

# year month day

