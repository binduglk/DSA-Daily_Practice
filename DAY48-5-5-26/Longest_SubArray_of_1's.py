# P48: Longest Subarray of 1s After Deleting One Element
# LeetCode 1493
# Problem: Delete exactly one element. Return the length of the longest subarray of 1s remaining.
# ============================================================
# Pattern: Variable Window — allow at most one 0 inside
# Deleting one element = we can have at most 1 zero in our window
# Time: O(n) | Space: O(1)

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        zeros = 0       # count of zeros in current window
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            # Window invalid: more than 1 zero → shrink
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # -1 because we must delete exactly one element
            max_len = max(max_len, right - left + 1 - 1)

        return max_len


# ============================
# 🔍 Testing
# ============================

sol = Solution()

print("Test 1:", sol.longestSubarray([1, 1, 0, 1]))
# Expected: 3 → delete the 0 → [1,1,1]

print("Test 2:", sol.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
# Expected: 5 → best window [1,1,1,0,1] after deleting one 0

print("Test 3:", sol.longestSubarray([1, 1, 1]))
# Expected: 2 → must delete one element, so [1,1]

print("Test 4:", sol.longestSubarray([0,0,0]))
# Expected: 0 → after deleting one 0, no 1s remain

print("Test 5:", sol.longestSubarray([1,0,1,1,0,1]))
# Expected: 4 → best window [1,1,0,1] after deleting one 0
