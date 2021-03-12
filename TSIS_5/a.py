a = []
with open('file1.txt', 'r') as f:
  for line in f:
  	a.append(len(line))
print(*a)
for i in range(1, len(a)):
	print("YES" if a[i-1] < a[i] else "NO")
