'''PROBLEM : Remove Duplicates from Sorted Array II
LeetCode 80
Problem: Given a sorted array, remove duplicates in-place such that each element appears at most twice. Return the new length.
Approach: Two pointers — allow at most 2 of each element.
Key Insight: nums[j] is safe to keep if it differs from nums[i-2] (the element written 2 positions back).
Time: O(n) | Space: O(1)'''

class Solution41:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0   # write pointer

        for num in nums:
            if i < 2 or num != nums[i - 2]:
                nums[i] = num
                i += 1

        return i


# --- TEST ---
sol41 = Solution41()
nums1 = [1,1,1,2,2,3]
length1 = sol41.removeDuplicates(nums1)
print(length1, nums1[:length1])  # Expected: 5, [1,1,2,2,3]

nums2 = [0,0,1,1,1,1,2,3,3]
length2 = sol41.removeDuplicates(nums2)
print(length2, nums2[:length2])  # Expected: 7, [0,0,1,1,2,3,3]

nums3 = [1,2,3,4,5]
length3 = sol41.removeDuplicates(nums3)
print(length3, nums3[:length3])  # Expected: 5, [1,2,3,4,5]
