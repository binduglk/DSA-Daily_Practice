# PROBLEM 29: 4Sum
# LeetCode 18
# Question: Given an array nums of n integers, 
# return all unique quadruplets [nums[a], nums[b], nums[c], nums[d]] 
# such that a, b, c, and d are distinct indices and 
# nums[a] + nums[b] + nums[c] + nums[d] == target.
# ============================================================

class Solution29:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3):
            # skip duplicate for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # skip duplicate for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        # skip duplicates for left and right
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result


# ============================
# 🔍 Testing
# ============================

sol = Solution29()

print("Test 1:", sol.fourSum([1,0,-1,0,-2,2], 0))
# Expected: [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]

print("Test 2:", sol.fourSum([2,2,2,2,2], 8))
# Expected: [[2,2,2,2]]

print("Test 3:", sol.fourSum([1,2,3,4,5,6,7,8], 18))
# Example: [[2,3,5,8], [3,4,5,6]]

print("Test 4:", sol.fourSum([-3,-1,0,2,4,5], 0))
# Expected: [[-3,-1,0,4]]
