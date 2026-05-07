'''PROBLEM : Smallest Divisor Given a Threshold
LeetCode 1283
Problem: Given an array nums and an integer threshold, return the smallest divisor such that the sum of ceil(nums[i]/divisor) ≤ threshold.
Approach: Binary search on divisor range [1, max(nums)].
Time: O(n log(max(nums))) | Space: O(1)'''

import math

def smallestDivisor(nums, threshold):
    def can(div):
        return sum(math.ceil(x / div) for x in nums) <= threshold

    low, high = 1, max(nums)
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if can(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


# --- TEST ---
print(smallestDivisor([1,2,5,9], 6))   # Expected: 5
print(smallestDivisor([44,22,33,11,1], 5)) # Expected: 44
