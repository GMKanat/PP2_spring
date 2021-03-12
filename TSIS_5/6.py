n = int(input())
a = input()
k = ""

for i in range(len(a)):
  if ord(a[i]) + n > 90:
    k += chr((ord(a[i]) + n)%90 + 64)
  else:
    k += chr((ord(a[i]) + n))
print(k)