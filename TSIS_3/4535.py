st = {'0'}
a = list(map(int, input().split()))
for i in range(len(a)):
	st.add(a[i])
print(len(st)-1)