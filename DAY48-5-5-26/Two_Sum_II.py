# PROBLEM 38: Two Sum II — Input Array is Sorted
# LeetCode 167
# Question: Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number. 
# Return the indices of the two numbers as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution.
# ============================================================

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]  # 1-indexed result
            elif total < target:
                left += 1
            else:
                right -= 1


# ============================
# 🔍 Testing
# ============================

sol = Solution()

print("Test 1:", sol.twoSum([2,7,11,15], 9))
# Expected: [1,2] → 2 + 7 = 9

print("Test 2:", sol.twoSum([2,3,4], 6))
# Expected: [1,3] → 2 + 4 = 6

print("Test 3:", sol.twoSum([-1,0], -1))
# Expected: [1,2] → -1 + 0 = -1

print("Test 4:", sol.twoSum([1,2,3,4,5,6], 10))
# Expected: [4,6] → 4 + 6 = 10

print("Test 5:", sol.twoSum([1,3,5,7,9,11], 14))
# Expected: [3,5] → 5 + 9 = 14
