# dutch National Flag (where it contains only 0's,1's,2's)

def Dutch(nums):
    low = 0
    mid = 0
    high = len(nums ) - 1

    while mid <= high:
        if nums[mid ] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:         # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums
print(Dutch([2,1,0,1,2]))