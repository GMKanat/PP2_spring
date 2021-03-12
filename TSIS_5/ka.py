n = int(input())
d = {'up' : 0, 'low' : 0 , 'num' : 0}
for i in range(n):
	a = input()
	for i in range(len(a)):
		if a[i].isupper():
			d['up'] += 1
		elif a[i].islower():
			d['low'] += 1
		elif a[i].isdigit():
			d['num'] += 1
print(d)


