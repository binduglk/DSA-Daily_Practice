'''PROBLEM : First and Last Occurrence of Element
LeetCode 34
Problem: Given a sorted array of integers, find the first and last position of a given target value.
Approach: Binary search twice — once for first occurrence, once for last.
Time: O(log n) | Space: O(1)'''

class Solution56:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first = self._firstOccurrence(nums, target)
        if first == -1:
            return [-1, -1]
        last = self._lastOccurrence(nums, target)
        return [first, last]

    def _firstOccurrence(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                ans = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def _lastOccurrence(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                ans = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return ans


# --- TEST ---
sol56 = Solution56()
print(sol56.searchRange([5,7,7,8,8,10], 8))  # Expected: [3,4]
print(sol56.searchRange([5,7,7,8,8,10], 6))  # Expected: [-1,-1]
print(sol56.searchRange([2,2,2,2], 2))       # Expected: [0,3]
