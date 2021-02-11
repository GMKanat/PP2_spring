a = list(map(int, input().split()))
mx = 10000
for i in range(len(a)):
	if a[i] > 0 and mx > a[i]:
		mx = a[i]
print(mx)