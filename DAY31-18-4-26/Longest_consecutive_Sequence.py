# PROBLEM 23: Longest Consecutive Sequence
# LeetCode 128
# Question: Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# ============================================================

class Solution23:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            print("Empty array → return 0")
            return 0

        num_set = set(nums)
        max_streak = 0
        print("Unique numbers:", num_set)

        for num in num_set:
            # only start counting if this is the beginning of a sequence
            if num - 1 not in num_set:
                print(f"Starting new sequence at {num}")
                current = num
                streak = 1

                # extend the sequence as far as possible
                while current + 1 in num_set:
                    current += 1
                    streak += 1
                    print(f"   Extended to {current}, streak={streak}")

                max_streak = max(max_streak, streak)
                print(f"   Sequence starting at {num} ended with length={streak}, max_streak={max_streak}")

        print("Final max_streak =", max_streak)
        return max_streak

# Testing
sol = Solution23()
print("Answer:", sol.longestConsecutive([100,4,200,1,3,2]))   # Expected 4 (sequence [1,2,3,4])
print("Answer:", sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # Expected 9 (sequence [0..8])
