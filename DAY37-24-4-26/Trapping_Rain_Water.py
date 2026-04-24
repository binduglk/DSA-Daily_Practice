# PROBLEM 40: Trapping Rain Water
# LeetCode 42
# Question: Given n non-negative integers representing an elevation map 
# where the width of each bar is 1, compute how much water it can trap after raining.
# ============================================================
# Approach: Two pointers with running max on each side
# Key: water at i = min(max_left, max_right) - height[i]
#      process whichever side has the smaller max — it's the bottleneck
# Time: O(n) | Space: O(1)

class Solution40:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        water = 0

        while left < right:
            if height[left] <= height[right]:
                # left side is the bottleneck
                if height[left] >= max_left:
                    max_left = height[left]     # new max — no water trapped here
                else:
                    water += max_left - height[left]   # water above this bar
                left += 1
            else:
                # right side is the bottleneck
                if height[right] >= max_right:
                    max_right = height[right]   # new max — no water trapped here
                else:
                    water += max_right - height[right]  # water above this bar
                right -= 1

        return water


# ============================
# 🔍 Testing
# ============================

sol = Solution40()

print("Test 1:", sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
# Expected: 6 → water trapped between bars

print("Test 2:", sol.trap([4,2,0,3,2,5]))
# Expected: 9 → water trapped in multiple valleys

print("Test 3:", sol.trap([1,0,2,1,0,1,3]))
# Expected: 6 → water trapped in dips

print("Test 4:", sol.trap([5,4,1,2]))
# Expected: 1 → small dip between 4 and 2

print("Test 5:", sol.trap([2,0,2]))
# Expected: 2 → water trapped between two walls
