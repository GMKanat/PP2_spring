import re

a = input()
k = input()
pattern = r'(?={})'.format(k)
m = re.finditer(pattern, a)

a = []
b = []
for i in m:
	a.append(i.start())
	b.append(i.start() + len(k)-1)
pafa = list(zip(a, b))
if(len(pafa) == 0):	print("(-1, -1)")
else: print(*pafa, sep = '\n')