'''PROBLEM : Search in Rotated Sorted Array
LeetCode 33 (no duplicates)
Problem: Given a rotated sorted array (no duplicates) and a target, return its index. If not found, return -1.
Approach: Binary search — one half is always sorted. Decide which half to search based on target’s range.
Time: O(log n) | Space: O(1)'''

class Solution58:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:  # left half sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:  # right half sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


# --- TEST ---
sol58 = Solution58()
print(sol58.search([4,5,6,7,0,1,2], 0))   # Expected: 4
print(sol58.search([4,5,6,7,0,1,2], 3))   # Expected: -1
print(sol58.search([1], 0))               # Expected: -1
