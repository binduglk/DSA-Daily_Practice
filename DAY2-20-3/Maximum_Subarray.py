'''Given an array of numbers (can include negatives), 
find the contiguous subarray that has the largest sum and return that sum.
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] Subarray [4, -1, 2, 1] has sum = 6 → Output: 6 
nums = [1] → Output: 1 nums = [5, 4, -1, 7, 8] → Output: 23 (whole array)'''

def max_subarray(nums):
    current_sum = nums[0]    # like currently bag/array is empty
    max_sum  = nums[0]       # initial maximun sum is 0

    for i in range(1,len(nums)):
        if current_sum < 0:            # bag / array has negative value ?
            current_sum = nums[i]      # start fresh
        else:
            current_sum += nums[i]     # if it is positive value in array
    
        if current_sum > max_sum:          # if cuurent value greater than max value
            max_sum = current_sum 

    return max_sum

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray([1]))                          
print(max_subarray([5,4,-1,7,8]))  
