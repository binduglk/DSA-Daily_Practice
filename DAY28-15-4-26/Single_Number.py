# PROBLEM 13: Single Number
# LeetCode 136
# Approach: XOR Trick — pairs cancel out (a ^ a = 0)
# Time: O(n) | Space: O(1)
# ============================================================

class Solution13:
    def singleNumber(self, nums: list[int]) -> int:
        xor = 0
        print("Initial XOR =", xor)
        for i, num in enumerate(nums):
            print(f"Step {i+1}: xor({xor}) ^ num({num}) = {xor ^ num}")
            xor ^= num               # duplicate pairs cancel to 0
            print(f"   Updated XOR = {xor}")
        print("Final Result =", xor)
        return xor                   # only the single number remains

# Testing
sol = Solution13()
print("Answer:", sol.singleNumber([4,1,2,1,2]))   # Expected 4
print("Answer:", sol.singleNumber([2,2,3]))       # Expected 3
print("Answer:", sol.singleNumber([1]))           # Expected 1