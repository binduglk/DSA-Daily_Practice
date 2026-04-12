# ---- Problem 1: Remove Duplicates from Sorted Array ----
# LeetCode #26
# Topic - Two Pointers

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        i = 0
        print(f"Initial array: {nums}")
        for j in range(1, len(nums)):
            print(f"Comparing nums[{j}]={nums[j]} with nums[{i}]={nums[i]}")
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                print(f"Found new unique element → placed {nums[j]} at index {i}")
            else:
                print(f"Duplicate {nums[j]} skipped")

        print(f"Final array with uniques at front: {nums[:i+1]}")
        return i + 1


# Testing
nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
length = sol.removeDuplicates(nums)
print(f"Length of unique array: {length}")
print(f"Array after removing duplicates: {nums[:length]}")