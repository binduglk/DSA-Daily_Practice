# PROBLEM 42: Sort Array by Parity
# LeetCode 905
# Question: Given an integer array nums, move all the even integers 
# to the beginning of the array followed by all the odd integers. 
# Return any array that satisfies this condition.
# ============================================================
# Approach: Two pointers swap — evens to front, odds to back
# Time: O(n) | Space: O(1)

class Solution42:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            # advance left until we hit an odd number
            while left < right and nums[left] % 2 == 0:
                left += 1
            # advance right until we hit an even number
            while left < right and nums[right] % 2 == 1:
                right -= 1

            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums


# ============================
# 🔍 Testing
# ============================

sol = Solution42()

print("Test 1:", sol.sortArrayByParity([3,1,2,4]))
# Expected: [2,4,3,1] → evens first, odds later

print("Test 2:", sol.sortArrayByParity([0]))
# Expected: [0] → single element

print("Test 3:", sol.sortArrayByParity([1,3,5,7]))
# Expected: [1,3,5,7] → all odds, no change

print("Test 4:", sol.sortArrayByParity([2,4,6,8]))
# Expected: [2,4,6,8] → all evens, no change

print("Test 5:", sol.sortArrayByParity([5,2,7,4,9,6]))
# Expected: [2,4,6,5,7,9] → evens grouped at front
