# Session 3 - Trapping Rain Water
# LeetCode #42
# Topic - Two Pointers
# Day 12

class Solution:
    def trap(self, height: list) -> int:
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water

# Testing
sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
print(sol.trap([4,2,0,3,2,5]))               # 9
print(sol.trap([1,0,1]))                      # 1