'''PROBLEM : Sliding Window Maximum
LeetCode 239
Problem: Given an array nums and an integer k, return the maximum value in each sliding window of size k.
Approach: Monotonic Deque (decreasing). Deque stores indices; front is always the max of current window. Remove from front if out of window; remove from back if smaller than incoming element.
Time: O(n) | Space: O(k).'''

from collections import deque

class Solution50:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        result = []

        for i in range(len(nums)):
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                result.append(nums[dq[0]])

        return result


# --- TEST ---
sol50 = Solution50()
print(sol50.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # Expected: [3,3,5,5,6,7]
print(sol50.maxSlidingWindow([1], 1))                  # Expected: [1]
print(sol50.maxSlidingWindow([9,10,9,-7,-4,-8,2,-6], 5)) # Expected: [10,10,9,2]
