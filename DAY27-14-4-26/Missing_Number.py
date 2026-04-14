# LeetCode Question: 268. Missing Number
# Problem: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
#          find the one number that is missing from the array.
# Time Complexity: O(n)
# Space Complexity: O(1)

def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Example usage
nums = [3, 0, 1]
print("Missing Number:", missingNumber(nums))  # Output: 2