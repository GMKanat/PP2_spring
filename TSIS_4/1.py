#https://www.hackerrank.com/challenges/introduction-to-regex/problem
import re as regex
n = int(input())
l = list()
for _ in range(n):
    s = input()
    x = regex.search("^(\+|\-|)([0-9]|)+\.+[0-9]+$", s)
    if x:
        l.append("True")
    else:
        l.append("False")
for x in l:
    print(x)
