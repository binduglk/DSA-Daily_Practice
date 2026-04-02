# Session 2 - Container With Most Water
# LeetCode #11
# Topic - Two Pointers
# Day 12

class Solution:
    def maxArea(self, height: list) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            water = width * h
            max_water = max(max_water, water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

# Testing
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))  # 49
print(sol.maxArea([1,1]))                  # 1
print(sol.maxArea([4,3,2,1,4]))           # 16