a = input()
b = input()
c = []
for i in range(len(a)):
	if a[i] == b:
		c.append(i)

# print(c)
d = []
for i in range(c[0]):
	d.append(c[0]-i)
# print(d)

for i in range(len(c)-1):
	for j in range(c[i], c[i+1]):
		d.append(min(abs(c[i]-j), abs(c[i+1]-j)))


for i in range(c[-1], len(a)):
	d.append(i - c[-1])
print(d)


# kbtupoints

# [2, 1, 0, 1, 2, 3, 2, 1, 0, 1]