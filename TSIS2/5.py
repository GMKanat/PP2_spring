class Solution(object):
    def subtractProductAndSum(self, n):
        a = 1
        b = 0
        while n!= 0:
            a *= n%10
            b += n%10
            n /= 10
        return a - b
        