'''PROBLEM : Search in Rotated Sorted Array II
LeetCode 81 (with duplicates)
Problem: Given a rotated sorted array (may contain duplicates) and a target, return True if found, else False.
Approach: Same as P58, but handle duplicates at boundaries (nums[low] == nums[mid] == nums[high]) by shrinking both ends.
Time: O(log n) average, O(n) worst | Space: O(1)'''

class Solution59:
    def search(self, nums: list[int], target: int) -> bool:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return True

            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

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

        return False


# --- TEST ---
sol59 = Solution59()
print(sol59.search([2,5,6,0,0,1,2], 0))   # Expected: True
print(sol59.search([2,5,6,0,0,1,2], 3))   # Expected: False
print(sol59.search([1,0,1,1,1], 0))       # Expected: True
