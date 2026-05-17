class Solution:
    def remove_duplicates(self, nums):

        left = 1

        for right in range(1, len(nums)):

            if nums[right] != nums[right - 1]:

                nums[left] = nums[right]

                left += 1

        return left


sol = Solution()

print(sol.remove_duplicates([1,1,2]))