d = {}
n = int(input())
for i in range(n):
	a = input()
	if not d.get(a):
		d[a] = 1
	else:
		d[a] += 1
print(d)