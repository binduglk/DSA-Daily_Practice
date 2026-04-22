# PROBLEM 34: Longest Subarray with Equal 0s and 1s
# Approach: Replace 0→-1, then longest subarray with sum 0
#           Prefix sum + HashMap (store FIRST occurrence of each sum)
# Time: O(n) | Space: O(n)
# ============================================================
# Question: Given a binary array, find the length of the longest subarray 
# that contains an equal number of 0s and 1s.

class Solution34:
    def longestEqualZeroOne(self, arr: list[int]) -> int:
        # store first index where each prefix sum was seen
        # initialise with {0: -1} meaning sum=0 exists before index 0
        prefix_map = {0: -1}
        running_sum = 0
        max_len = 0

        for i, val in enumerate(arr):
            # treat 0 as -1 so equal 0s and 1s cancel to 0
            running_sum += 1 if val == 1 else -1

            if running_sum in prefix_map:
                # same prefix sum seen before → subarray between sums to 0
                length = i - prefix_map[running_sum]
                max_len = max(max_len, length)
            else:
                # only store FIRST occurrence — longer subarray is always better
                prefix_map[running_sum] = i

        return max_len


# ============================
# 🔍 Testing
# ============================

sol = Solution34()

print("Test 1:", sol.longestEqualZeroOne([0,1]))
# Expected: 2 → subarray [0,1]

print("Test 2:", sol.longestEqualZeroOne([0,1,0]))
# Expected: 2 → subarray [0,1] or [1,0]

print("Test 3:", sol.longestEqualZeroOne([0,0,1,1,0]))
# Expected: 4 → subarray [0,1,1,0]

print("Test 4:", sol.longestEqualZeroOne([1,1,1,0,0,0]))
# Expected: 6 → whole array has equal 0s and 1s

print("Test 5:", sol.longestEqualZeroOne([1,0,1,1,0,0,1]))
# Expected: 6 → subarray [0,1,1,0,0,1]
