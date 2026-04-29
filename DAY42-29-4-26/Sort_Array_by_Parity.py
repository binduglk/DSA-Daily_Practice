'''PROBLEM : Sort Array by Parity
LeetCode 905
Problem: Given an array of integers, move all even integers to the beginning followed by all odd integers.
Approach: Two pointers swap — evens to front, odds to back.
Time: O(n) | Space: O(1)'''

class Solution42:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            while left < right and nums[left] % 2 == 0:
                left += 1
            while left < right and nums[right] % 2 == 1:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums


# --- TEST ---
sol42 = Solution42()
print(sol42.sortArrayByParity([3,1,2,4]))   # Expected: [2,4,3,1]
print(sol42.sortArrayByParity([0]))         # Expected: [0]
print(sol42.sortArrayByParity([1,3,5,7]))   # Expected: [1,3,5,7]
print(sol42.sortArrayByParity([2,4,6,8]))   # Expected: [2,4,6,8]
