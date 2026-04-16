# PROBLEM 18: Maximum Subarray (Kadane's Algorithm)
# LeetCode 53
# Question: Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.
# ============================================================

class Solution18:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        print(f"Initial: current_sum={current_sum}, max_sum={max_sum}")

        for i, num in enumerate(nums[1:], start=1):
            # extend current subarray OR start fresh from current element
            new_sum = max(num, current_sum + num)
            print(f"Index={i}, Num={num}, Extend={current_sum+num}, Restart={num}, Chosen={new_sum}")
            current_sum = new_sum
            max_sum = max(max_sum, current_sum)
            print(f"   Updated: current_sum={current_sum}, max_sum={max_sum}")

        print("Final max_sum =", max_sum)
        return max_sum

# Testing
sol = Solution18()
print("Answer:", sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Expected 6 (subarray [4,-1,2,1])
print("Answer:", sol.maxSubArray([1]))                      # Expected 1
print("Answer:", sol.maxSubArray([5,4,-1,7,8]))             # Expected 23
