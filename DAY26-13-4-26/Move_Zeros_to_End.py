class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        j = 0  # Pointer for non-zero elements
        for i in range(len(nums)):
            print(f"Step {i}: nums = {nums}, j = {j}")
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                print(f"  Swapped nums[{i}] and nums[{j}] → {nums}")
                j += 1
        print("Final result:", nums)


# Example usage
nums = [0, 1, 0, 3, 12]
print("Original list:", nums)
Solution().moveZeroes(nums)