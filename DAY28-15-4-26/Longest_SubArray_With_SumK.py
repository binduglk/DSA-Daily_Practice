# PROBLEM 14: Longest Subarray with Sum K (Positive numbers)
# Approach: Sliding Window (two pointers)
# Time: O(n) | Space: O(1)
# ============================================================

class Solution14:
    def longestSubarrayWithSumK(self, arr: list[int], k: int) -> int:
        left = 0
        window_sum = 0
        max_len = 0

        for right in range(len(arr)):
            window_sum += arr[right]             # expand window to the right
            print(f"Right={right}, Added={arr[right]}, WindowSum={window_sum}")

            while window_sum > k and left <= right:
                print(f"   Shrinking: Removing={arr[left]} at Left={left}")
                window_sum -= arr[left]          # shrink from the left
                left += 1
                print(f"   New Left={left}, WindowSum={window_sum}")

            if window_sum == k:
                current_len = right - left + 1
                max_len = max(max_len, current_len)
                print(f"   Found sum=k at [{left},{right}], Length={current_len}, MaxLen={max_len}")

        print("Final MaxLen =", max_len)
        return max_len

# Testing
sol = Solution14()
print("Answer:", sol.longestSubarrayWithSumK([1,2,1,1,1,3,2,1], 3))   # Expected 3
print("Answer:", sol.longestSubarrayWithSumK([1,2,3,4,5], 11))        # Expected 3
print("Answer:", sol.longestSubarrayWithSumK([2,3,5], 5))             # Expected 1