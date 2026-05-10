'''Problem : Maximum Subarray
Platform: LeetCode 53
Question:  
Find the contiguous subarray with the largest sum and return its sum.

Approach
Use Kadane’s Algorithm.
Keep adding elements to a running sum.
If sum becomes negative → reset to 0.
Track maximum sum encountered.
Time Complexity: O(n).'''

def maxSubArray(nums):
    curr = 0
    maxi = nums[0]
    for n in nums:
        curr += n
        maxi = max(maxi, curr)
        if curr < 0:
            curr = 0
    return maxi

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
