import re
s = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall('[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]([[aeiouAEIOU]{2,})[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]', input(), re.DEBUG)
if a:
    for i in a:
        print(i)
else:
    print(-1)