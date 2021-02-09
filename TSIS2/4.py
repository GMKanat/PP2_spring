class Solution(object):
    def largestAltitude(self, gain):
        s = 0
        i = 0
        mx = 0
        while i < len(gain):
            s += gain[i]
            if s > mx:
                mx = s
            i += 1
        return mx
        