a = list(map(int, input().split()))
cnt = 0
for i in range(len(a)):
	if a[i] != 0:
		print(a[i], end = " ")
	else:
		cnt += 1
for i in range(cnt):
	print(0, end = " ")