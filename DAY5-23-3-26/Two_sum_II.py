'''Given a sorted array and a target, find two numbers that add up to target. 
Return their positions starting from 1 (not 0). Must use O(1) space — no dictionary!
numbers = [2,7,11,15], target = 9 → [1,2] 
numbers = [2,3,4], target = 6 → [1,3] numbers = [-1,0], target = -1 → [1,2]'''

def two_sum_2(nums,target):
    left = 0
    right = len(nums)-1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return [left+1,right+1]
        elif total > target:
            right -= 1
        else:
            left += 1

    return[]

print(two_sum_2([12,13,15,18],33))
print(two_sum_2([1,2,3,4,6,],9))

