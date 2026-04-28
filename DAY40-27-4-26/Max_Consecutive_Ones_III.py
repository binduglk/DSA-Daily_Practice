# P51: Max Consecutive Ones III
# LeetCode 1004
# Problem: Given a binary array nums and an integer k,
# return the maximum number of consecutive 1s in the array
# if you can flip at most k zeros.
# ============================================================
# Pattern: Variable Window — allow at most k zeros (flips)
# Time: O(n) | Space: O(1)

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zeros = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            # Too many zeros → shrink
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


# ============================
# 🔍 Testing
# ============================

sol = Solution()

print("Test 1:", sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
# Expected: 6 → flip two zeros in the middle

print("Test 2:", sol.longestOnes([0,0,1,1,1,0,0], 1))
# Expected: 4 → best window [0,1,1,1] after flipping one zero

print("Test 3:", sol.longestOnes([1,1,1,1], 0))
# Expected: 4 → no flips needed

print("Test 4:", sol.longestOnes([0,0,0,0], 2))
# Expected: 2 → flip any two zeros

print("Test 5:", sol.longestOnes([1,0,1,0,1,0,1], 3))
# Expected: 7 → flip all three zeros
