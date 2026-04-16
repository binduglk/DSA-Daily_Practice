# PROBLEM 17: Majority Element
# LeetCode 169
# Question: Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
# ============================================================

class Solution17:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0

        print("Initial candidate=None, count=0")

        for i, num in enumerate(nums):
            if count == 0:
                candidate = num          # start fresh with new candidate
                print(f"Step {i}: count=0 → new candidate={candidate}")
            if num == candidate:
                count += 1               # vote for candidate
                print(f"Step {i}: num={num} == candidate → count={count}")
            else:
                count -= 1               # vote against candidate
                print(f"Step {i}: num={num} != candidate → count={count}")

        print("Final candidate =", candidate)
        return candidate                 # majority always survives

# Testing
sol = Solution17()
print("Answer:", sol.majorityElement([3,2,3]))        # Expected 3
print("Answer:", sol.majorityElement([2,2,1,1,1,2,2])) # Expected 2
