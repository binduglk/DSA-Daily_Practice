class Solution:
    def maxSubArray(self, nums):

        cur = 0
        maxi = nums[0]

        for n in nums:

            cur += n

            maxi = max(maxi, cur)

            if cur < 0:
                cur = 0

        return maxi