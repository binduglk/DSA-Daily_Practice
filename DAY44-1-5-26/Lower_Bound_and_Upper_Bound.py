'''PROBLEM : Lower Bound and Upper Bound
Concept Problem (Striver’s A2Z)
Problem: Implement lower bound and upper bound functions.
Lower bound: First index where nums[i] >= target.
Upper bound: First index where nums[i] > target.
Approach: Binary search variant.
Time: O(log n) | Space: O(1)'''

class Solution53:
    def lowerBound(self, nums: list[int], target: int) -> int:
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

    def upperBound(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        ans = len(nums)
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lb = self.lowerBound(nums, target)
        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]
        ub = self.upperBound(nums, target) - 1
        return [lb, ub]


# --- TEST ---
sol53 = Solution53()
print(sol53.lowerBound([1,2,4,4,5,6], 4))   # Expected: 2
print(sol53.upperBound([1,2,4,4,5,6], 4))   # Expected: 4
print(sol53.searchRange([5,7,7,8,8,10], 8)) # Expected: [3,4]
print(sol53.searchRange([5,7,7,8,8,10], 6)) # Expected: [-1,-1]
