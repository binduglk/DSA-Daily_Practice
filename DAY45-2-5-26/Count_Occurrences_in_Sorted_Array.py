'''PROBLEM : Count Occurrences in Sorted Array
Concept Problem (Binary Search Variant)
Problem: Count how many times a target appears in a sorted array.
Approach: Use first and last occurrence indices → count = last - first + 1.
Time: O(log n) | Space: O(1)'''

class Solution57:
    def countOccurrences(self, nums: list[int], target: int) -> int:
        first = self._firstOccurrence(nums, target)
        if first == -1:
            return 0
        last = self._lastOccurrence(nums, target)
        return last - first + 1

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
sol57 = Solution57()
print(sol57.countOccurrences([1,2,2,2,3,4], 2))  # Expected: 3
print(sol57.countOccurrences([1,1,1,1], 1))      # Expected: 4
print(sol57.countOccurrences([1,2,3,4,5], 6))    # Expected: 0
