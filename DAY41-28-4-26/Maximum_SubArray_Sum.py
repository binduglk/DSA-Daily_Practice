# PROBLEM 43: Maximum Sum Subarray of Size K
# Approach: Fixed sliding window — one pass after initial build
# Time: O(n) | Space: O(1)

class Solution43:
    def maxSumSubarrayK(self, arr: list[int], k: int) -> int:
        n = len(arr)
        if n < k:
            return -1

        # Build the first window
        window_sum = sum(arr[:k])
        max_sum = window_sum

        # Slide the window
        for i in range(k, n):
            window_sum += arr[i] - arr[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum


# --- TEST ---
sol43 = Solution43()
print(sol43.maxSumSubarrayK([2,1,5,1,3,2], 3))   # Expected: 9
print(sol43.maxSumSubarrayK([2,3,4,1,5], 2))     # Expected: 7
