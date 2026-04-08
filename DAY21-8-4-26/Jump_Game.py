# Session 2 - Jump Game
# LeetCode #55
# Topic - Greedy
# Day 18

class Solution:
    def canJump(self, nums: list) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:       # stuck!
                return False
            max_reach = max(max_reach, i + nums[i])

        return True

# Testing
sol = Solution()
print(sol.canJump([2,3,1,1,4]))   # True
print(sol.canJump([3,2,1,0,4]))   # False
print(sol.canJump([0]))            # True
print(sol.canJump([1,0,0]))        # False

'''🎬 Trace:
nums = [3,2,1,0,4]
max_reach = 0

i=0: 0<=0 ✅ max_reach=max(0,0+3)=3
i=1: 1<=3 ✅ max_reach=max(3,1+2)=3
i=2: 2<=3 ✅ max_reach=max(3,2+1)=3
i=3: 3<=3 ✅ max_reach=max(3,3+0)=3
i=4: 4>3  ❌ return False! ✅'''