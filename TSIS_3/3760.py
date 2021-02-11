ar = int(input())
diction = {}
for i in range(ar):
	a, b = (str(i) for i in input().split())
	diction[a] = b
	diction[b] = a
br = input()
print(diction[br])