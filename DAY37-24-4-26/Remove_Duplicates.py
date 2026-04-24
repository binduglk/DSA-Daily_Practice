# PROBLEM 41: Remove Duplicates from Sorted Array II
# LeetCode 80
# Question: Given an integer array nums sorted in non-decreasing order, 
# remove some duplicates in-place such that each unique element appears at most twice. 
# The relative order of the elements should be kept the same. 
# Return the new length of nums after removal.
# ============================================================
# Approach: Two pointers — allow at most 2 of each element
# Key insight: nums[j] is safe to keep if it differs from nums[i-2]
#              (the element written 2 positions back)
# Time: O(n) | Space: O(1)

class Solution41:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0   # write pointer — where to place the next valid element

        for num in nums:
            # first two positions are always valid
            # beyond that: only write if current != element two slots back
            if i < 2 or num != nums[i - 2]:
                nums[i] = num
                i += 1

        return i    # new length


# ============================
# 🔍 Testing
# ============================

sol = Solution41()

nums1 = [1,1,1,2,2,3]
length1 = sol.removeDuplicates(nums1)
print("Test 1:", length1, nums1[:length1])
# Expected: 5, [1,1,2,2,3]

nums2 = [0,0,1,1,1,1,2,3,3]
length2 = sol.removeDuplicates(nums2)
print("Test 2:", length2, nums2[:length2])
# Expected: 7, [0,0,1,1,2,3,3]

nums3 = [1,2,3,4,5]
length3 = sol.removeDuplicates(nums3)
print("Test 3:", length3, nums3[:length3])
# Expected: 5, [1,2,3,4,5] (no duplicates)

nums4 = [1,1,1,1,1]
length4 = sol.removeDuplicates(nums4)
print("Test 4:", length4, nums4[:length4])
# Expected: 2, [1,1]

nums5 = [2,2,3,3,3,4,4,4,4]
length5 = sol.removeDuplicates(nums5)
print("Test 5:", length5, nums5[:length5])
# Expected: 6, [2,2,3,3,4,4]
