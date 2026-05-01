'''PROBLEM : Search Insert Position
LeetCode 35
Problem: Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be inserted in order.
Approach: Lower bound — first index where nums[i] >= target.
Time: O(log n) | Space: O(1)'''

class Solution54:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        ans = len(nums)
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


# --- TEST ---
sol54 = Solution54()
print(sol54.searchInsert([1,3,5,6], 5))  # Expected: 2
print(sol54.searchInsert([1,3,5,6], 2))  # Expected: 1
print(sol54.searchInsert([1,3,5,6], 7))  # Expected: 4
print(sol54.searchInsert([1,3,5,6], 0))  # Expected: 0
