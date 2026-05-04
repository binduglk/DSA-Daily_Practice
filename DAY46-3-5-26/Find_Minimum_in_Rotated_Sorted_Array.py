'''PROBLEM : Find Minimum in Rotated Sorted Array
LeetCode 153 (no duplicates)
Problem: Given a rotated sorted array (no duplicates), find the minimum element.
Approach: The minimum is always in the unsorted half. If left half is sorted, min candidate = nums[low]; else min candidate = nums[mid]. Search the unsorted half.
Time: O(log n) | Space: O(1)'''

class Solution60:
    def findMin(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1
        min_val = float('inf')

        while low <= high:
            mid = low + (high - low) // 2

            if nums[low] <= nums[mid]:  # left half sorted
                min_val = min(min_val, nums[low])
                low = mid + 1
            else:  # right half sorted
                min_val = min(min_val, nums[mid])
                high = mid - 1

        return min_val


# --- TEST ---
sol60 = Solution60()
print(sol60.findMin([3,4,5,1,2]))       # Expected: 1
print(sol60.findMin([4,5,6,7,0,1,2]))   # Expected: 0
print(sol60.findMin([11,13,15,17]))     # Expected: 11
