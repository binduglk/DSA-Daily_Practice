'''Given an array containing n distinct numbers taken from 0, 1, 2 ... n, 
find the one number that is missing from the array.
nums = [3, 0, 1] → Output: 2 (missing 2) nums = [0, 1] → Output: 2 (missing 2) 
nums = [9,6,4,2,3,5,7,0,1] → Output: 8'''

def missing_num(nums):
    n = len(nums)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum

print(missing_num([1,3,4,0,5,6,7]))         # we should give only 0-9 and also there should be only one num missing
print(missing_num([1,2,3,4,0,5,6,7,9])) 
print(missing_num([1,2,4,0,5,6]))    