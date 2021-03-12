# https://www.hackerrank.com/challenges/re-group-groups/problem

import re

pattern = r'(\w+)@(\w+)\.(\w+)'
m = re.match(pattern, 'username@hackerrank.com')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
for i in m.groups():
    print(i)
