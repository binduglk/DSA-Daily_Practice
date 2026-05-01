'''PROBLEM : Binary Search on Sorted Array
LeetCode 704
Problem: Given a sorted array of integers and a target value, return the index if the target is found. If not, return -1.
Approach: Classic binary search — halve the search space each step.
Time: O(log n) | Space: O(1)'''

class Solution52:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1


# --- TEST ---
sol52 = Solution52()
print(sol52.search([-1,0,3,5,9,12], 9))   # Expected: 4
print(sol52.search([-1,0,3,5,9,12], 2))   # Expected: -1
print(sol52.search([1,2,3,4,5], 1))       # Expected: 0
