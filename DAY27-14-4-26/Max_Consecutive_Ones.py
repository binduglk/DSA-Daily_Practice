# LeetCode Question: 485. Max Consecutive Ones
# Problem: Given a binary array, find the maximum number of consecutive 1s.
# Time Complexity: O(n)
# Space Complexity: O(1)

def findMaxConsecutiveOnes(nums):
    max_count = 0
    current_count = 0
    
    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    
    return max_count

# Example usage
nums = [1, 1, 0, 1, 1, 1]
print("Max Consecutive Ones:", findMaxConsecutiveOnes(nums))  # Output: 3