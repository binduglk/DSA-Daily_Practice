'''PROBLEM : Floor and Ceil in Sorted Array
Concept Problem (Binary Search Variant)
Problem: Find the floor and ceil of a target in a sorted array.
Floor: Largest element ≤ target.
Ceil: Smallest element ≥ target.
Approach: Binary search variant — adjust pointers based on comparisons.
Time: O(log n) | Space: O(1)'''

class Solution55:
    def floorCeil(self, nums: list[int], target: int) -> tuple:
        return self._floor(nums, target), self._ceil(nums, target)

    def _floor(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= target:
                ans = nums[mid]
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def _ceil(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                ans = nums[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ans


# --- TEST ---
sol55 = Solution55()
print(sol55.floorCeil([1,2,4,6,10], 5))   # Expected: (4,6)
print(sol55.floorCeil([1,2,4,6,10], 11))  # Expected: (10,-1)
print(sol55.floorCeil([1,2,4,6,10], 0))   # Expected: (-1,1)
