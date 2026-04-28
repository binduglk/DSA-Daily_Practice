# PROBLEM 36: Longest Consecutive Sequence (HashMap approach)
# LeetCode 128
# Question: Given an unsorted array of integers nums, 
# return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# ============================================================

class Solution36:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)         # O(1) membership check
        max_streak = 0

        for num in num_set:
            # only start counting from the beginning of a sequence
            # a sequence start has no predecessor in the set
            if num - 1 not in num_set:
                current = num
                streak = 1

                while current + 1 in num_set:
                    current += 1
                    streak += 1

                max_streak = max(max_streak, streak)

        return max_streak


# ============================
# 🔍 Testing
# ============================

sol = Solution36()

print("Test 1:", sol.longestConsecutive([100,4,200,1,3,2]))
# Expected: 4 → sequence [1,2,3,4]

print("Test 2:", sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
# Expected: 9 → sequence [0,1,2,3,4,5,6,7,8]

print("Test 3:", sol.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
# Expected: 7 → sequence [-1,0,1,3,4,5,6,7,8] → longest is length 7

print("Test 4:", sol.longestConsecutive([]))
# Expected: 0 → empty array

print("Test 5:", sol.longestConsecutive([1,2,0,1]))
# Expected: 3 → sequence [0,1,2]
