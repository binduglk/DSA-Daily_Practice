class Solution:
    def findMaxAverage(self, nums, k):

        window = sum(nums[:k])

        maxi = window

        for i in range(k, len(nums)):

            window += nums[i] - nums[i-k]

            maxi = max(maxi, window)

        return maxi / k


sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))