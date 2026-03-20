'''Move all zeroes in the array to the end while keeping the order of non-zero numbers the same. 
Do it in-place — no new array allowed.
Input : [0, 1, 0, 3, 12] → Output: [1, 3, 12, 0, 0] 
Input : [0, 0, 1] → Output: [1, 0, 0] Input : [1, 2, 3] → Output: [1, 2, 3]'''

def move_zeros(nums):
    insert_pos = 0        # initial inserting initial position is 0

    for num in nums:      # pushing all zeros to front
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    
    while insert_pos < len(nums):      # filling the rest with 0
        nums[insert_pos] = 0
        insert_pos += 1

    return nums

print(move_zeros([1,0,2,3,0,12]))
print(move_zeros([0,0,5,0,2]))