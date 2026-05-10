'''Problem : Two Sum
Platform: LeetCode 1
Question:  
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
Approach:
Use a hashmap/dictionary.
For each number, check if target - current exists in the dictionary.
If yes → return indices.
Else store current number with its index.
Time Complexity: O(n).'''

def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        rem = target - nums[i]
        if rem in d:
            return [d[rem], i]
        d[nums[i]] = i

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))  # [0,1]
