'''PROBLEM : Single Element in a Sorted Array
LeetCode 540
Problem: Every element appears exactly twice except one — find it.
Approach: Binary search on index parity
Before the single element: pairs start at even indices.
After the single element: pairs start at odd indices.
Time: O(log n) | Space: O(1)'''

class Solution71:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid
        return nums[low]


# --- TEST ---
sol71 = Solution71()
print(sol71.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))  # Expected: 2
print(sol71.singleNonDuplicate([3,3,7,7,10,11,11]))   # Expected: 10
