
a = [1, 3, 4, 5]

b = set()
for i in range(len(a)):
	c = []
	for j in range(i, len(a)):
		for k in range(i, j):
			c.append(a[i])
	b.add(c)
print(b)