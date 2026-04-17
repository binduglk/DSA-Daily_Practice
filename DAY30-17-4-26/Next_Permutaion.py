# PROBLEM 21: Next Permutation
# LeetCode 31
# Question: A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
# The next permutation of an array is the next lexicographically greater permutation of its integer sequence.
# If no such permutation exists, rearrange it into the lowest possible order (i.e., sorted in ascending order).
# ============================================================

class Solution21:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Steps:
        1. Find break point i: rightmost index where nums[i] < nums[i+1]
        2. Find swap target j: rightmost index where nums[j] > nums[i]
           Swap nums[i] and nums[j]
        3. Reverse the suffix starting at i+1
        If no break point: entire array is descending, reverse all.
        """
        n = len(nums)
        i = n - 2

        print("Initial:", nums)

        # Step 1: find break point from right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        print(f"Break point index i={i}")

        if i >= 0:
            # Step 2: find rightmost element greater than nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            print(f"Swap indices i={i}, j={j}, values {nums[i]} <-> {nums[j]}")
            nums[i], nums[j] = nums[j], nums[i]  # swap

        # Step 3: reverse suffix after break point (or entire array if i = -1)
        left = i + 1
        right = n - 1
        print(f"Reversing suffix from index {left} to {right}")
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            print("   Current:", nums)

        print("Final:", nums)

# Testing
sol = Solution21()
arr = [1,2,3]
sol.nextPermutation(arr)
print("Answer:", arr)   # Expected [1,3,2]

arr = [3,2,1]
sol.nextPermutation(arr)
print("Answer:", arr)   # Expected [1,2,3]

arr = [1,1,5]
sol.nextPermutation(arr)
print("Answer:", arr)   # Expected [1,5,1]
