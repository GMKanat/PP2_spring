class Solution(object):
    def numIdenticalPairs(self, nums):
        n = len(nums)
        ans = 0
        for i in range(n):
          for j in range(i + 1, n):
            if nums[i] == nums[j]: ans += 1
        return ans
        