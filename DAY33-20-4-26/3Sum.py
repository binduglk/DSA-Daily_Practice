# PROBLEM 28: 3Sum
# LeetCode 15
# Question: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.
# The solution set must not contain duplicate triplets.
# ============================================================

class Solution28:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        print("Sorted nums:", nums)

        for i in range(len(nums) - 2):
            # skip duplicate values for the fixed element
            if i > 0 and nums[i] == nums[i - 1]:
                print(f"Skip duplicate fixed element at index {i}, value={nums[i]}")
                continue

            left = i + 1
            right = len(nums) - 1
            print(f"\nFixed index={i}, value={nums[i]}, left={left}, right={right}")

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                print(f"   Trying triplet ({nums[i]}, {nums[left]}, {nums[right]}) → total={total}")

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    print(f"   Found triplet: {result[-1]}")

                    # skip duplicates for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                        print(f"   Skip duplicate left at {left}")
                    # skip duplicates for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        print(f"   Skip duplicate right at {right}")

                    left += 1
                    right -= 1
                    print(f"   Move pointers → left={left}, right={right}")

                elif total < 0:
                    print("   Sum too small → move left forward")
                    left += 1       # sum too small, need bigger value
                else:
                    print("   Sum too big → move right backward")
                    right -= 1      # sum too big, need smaller value

        print("\nFinal result:", result)
        return result

# Testing
sol = Solution28()
print("Answer:", sol.threeSum([-1,0,1,2,-1,-4]))  
# Expected [[-1,-1,2],[-1,0,1]]
