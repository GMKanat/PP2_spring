# https://www.hackerrank.com/challenges/re-group-groups/problem
import re
pattern = r'([a-zA-Z0-9])\1+'

m = re.search(pattern, input())
if m:
    print(m.group(1))
else:
    print(-1)