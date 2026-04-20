# PROBLEM 30: Container With Most Water
# LeetCode 11
# Question: You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# ============================================================

class Solution30:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # water trapped = min height × width
            water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, water)

            # move the shorter wall inward — keeping the taller one
            # gives the only chance of finding a larger area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


# ============================
# 🔍 Testing
# ============================

sol = Solution30()

print("Test 1:", sol.maxArea([1,8,6,2,5,4,8,3,7]))
# Expected: 49 (between lines at index 1 and 8)

print("Test 2:", sol.maxArea([1,1]))
# Expected: 1 (only two lines)

print("Test 3:", sol.maxArea([4,3,2,1,4]))
# Expected: 16 (between lines at index 0 and 4)

print("Test 4:", sol.maxArea([1,2,1]))
# Expected: 2 (between lines at index 0 and 2)
