'''PROBLEM : Trapping Rain Water
LeetCode 42
Problem: Given n non-negative integers representing an elevation map, compute how much water it can trap after raining.
Approach: Two pointers with running max on each side.
Key Insight: Water at i = min(max_left, max_right) - height[i]. Process whichever side has the smaller max — it’s the bottleneck.
Time: O(n) | Space: O(1)'''

class Solution40:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        water = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    water += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    water += max_right - height[right]
                right -= 1

        return water

# --- TEST ---
sol40 = Solution40()
print(sol40.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Expected: 6
print(sol40.trap([4,2,0,3,2,5]))              # Expected: 9
print(sol40.trap([1,2,3,4,5]))                # Expected: 0