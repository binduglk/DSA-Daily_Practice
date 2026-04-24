# PROBLEM 39: 3Sum Closest
# LeetCode 16
# Question: Given an integer array nums of length n and an integer target, 
# find three integers in nums such that the sum is closest to target. 
# Return the sum of the three integers. You may assume that each input 
# would have exactly one solution.
# ============================================================

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(closest - target):
                    closest = total

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total  # exact match

        return closest


# ============================
# 🔍 Testing
# ============================

sol = Solution()

print("Test 1:", sol.threeSumClosest([-1,2,1,-4], 1))
# Expected: 2 → closest sum is (-1 + 2 + 1)

print("Test 2:", sol.threeSumClosest([0,0,0], 1))
# Expected: 0 → only possible sum

print("Test 3:", sol.threeSumClosest([1,1,1,0], -100))
# Expected: 2 → closest sum is (0+1+1)

print("Test 4:", sol.threeSumClosest([1,2,5,10,11], 12))
# Expected: 13 → closest sum is (1+2+10)

print("Test 5:", sol.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))
# Expected: -2 → exact match possible
