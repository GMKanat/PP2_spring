# https://www.hackerrank.com/challenges/introduction-to-regex

import re
for _ in range(int(input())):
    txt = input()
    pattern = r"^[-+]?[0-9]*\.[0-9]+$"
    x = re.search(pattern, txt)
    if x:
        print("True")
    else:
        print("False")
