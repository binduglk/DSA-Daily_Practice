# Session 1 - House Robber
# LeetCode #198
# Topic - 1D Dynamic Programming
# Day 14

class Solution:
    def rob(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]

        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current

        return prev1

# Testing
sol = Solution()
print(sol.rob([1,2,3,1]))      # 4
print(sol.rob([2,7,9,3,1]))    # 12
print(sol.rob([2,1]))           # 2