'''Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, return its index. Otherwise, return -1.'''

def search(nums,target):                   # ([1,3,5,6,7,8,9],5)
    left = 0                               # left = 0
    right = len(nums)-1                    # right = 6

    while left <= right:                   # 0 <= 6 true
        mid = (left+right)//2              # mid = 3
    
        if nums[mid] == target:            # nums[3]i.e 6 == 5 false
            return mid
        if nums[mid] < target:             # 6 < 5  false
            left = mid + 1                 # left = 0
        else:
            right = mid - 1               # right = 2 next iterate for each number until target number becomes mid 
    
    return -1

print(search([1,3,5,6,7,8,9],5))         # 2
print(search([-1,0,3,5,9,12],9))         # 4