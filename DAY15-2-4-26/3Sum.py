# Session 1 - 3Sum
# LeetCode #15
# Topic - Two Pointers + Sorting
# Day 12

class Solution:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        result = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue                    # skip duplicates!

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1           # skip duplicates
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1          # skip duplicates
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

# Testing
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
print(sol.threeSum([0,1,1]))            # []
print(sol.threeSum([0,0,0]))            # [[0,0,0]]