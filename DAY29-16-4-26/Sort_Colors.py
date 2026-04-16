# PROBLEM 16: Sort Colors
# LeetCode 75
# Question: Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent,
# with colors in the order red (0), white (1), and blue (2).
# ============================================================

class Solution16:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Invariant:
            nums[0..low-1]   = all 0s
            nums[low..mid-1] = all 1s
            nums[mid..high]  = unsorted
            nums[high+1..n]  = all 2s
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        print("Initial:", nums)

        while mid <= high:
            print(f"low={low}, mid={mid}, high={high}, nums={nums}")
            if nums[mid] == 0:
                print(f"   nums[mid]=0 → swap nums[{low}] and nums[{mid}]")
                nums[low], nums[mid] = nums[mid], nums[low]  # send 0 to front
                low += 1
                mid += 1
            elif nums[mid] == 1:
                print(f"   nums[mid]=1 → move mid forward")
                mid += 1                                      # 1 is in correct zone
            else:
                print(f"   nums[mid]=2 → swap nums[{mid}] and nums[{high}]")
                nums[mid], nums[high] = nums[high], nums[mid] # send 2 to back
                high -= 1
                # do NOT advance mid — swapped value from high is unseen

        print("Final:", nums)

# Testing
sol = Solution16()
arr = [2,0,2,1,1,0]
sol.sortColors(arr)
print("Answer:", arr)   # Expected [0,0,1,1,2,2]
