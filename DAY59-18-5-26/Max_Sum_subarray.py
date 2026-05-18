class Solution:

    def maxSumSubarray(self, nums, k):

        window = sum(nums[:k])
        maxi = window

        for right in range(k, len(nums)):

            window += nums[right] - nums[right-k]

            maxi = max(maxi, window)

        return maxi


sol = Solution()

print(sol.maxSumSubarray([1,2,3,4,5], 2))