# PROBLEM 20: Rearrange Array Elements by Sign
# LeetCode 2149
# Question: You are given a 0-indexed integer array nums of even length 
# consisting of an equal number of positive and negative integers.
# You should rearrange the elements of nums such that the modified array follows:
#   - Every consecutive pair of integers have opposite signs.
#   - For all integers with the same sign, the order in which they appear in nums is preserved.
#   - The rearranged array begins with a positive integer.
# Return the modified array.
# ============================================================

class Solution20:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        pos_idx = 0   # next available even index for positives
        neg_idx = 1   # next available odd index for negatives

        print("Initial result:", result)

        for i, num in enumerate(nums):
            if num > 0:
                result[pos_idx] = num
                print(f"Step {i}: num={num} → placed at pos_idx={pos_idx}")
                pos_idx += 2                    # jump to next even slot
            else:
                result[neg_idx] = num
                print(f"Step {i}: num={num} → placed at neg_idx={neg_idx}")
                neg_idx += 2                    # jump to next odd slot
            print("   Current result:", result)

        print("Final result:", result)
        return result

# Testing
sol = Solution20()
print("Answer:", sol.rearrangeArray([3,1,-2,-5,2,-4]))  
# Expected [3,-2,1,-5,2,-4]
