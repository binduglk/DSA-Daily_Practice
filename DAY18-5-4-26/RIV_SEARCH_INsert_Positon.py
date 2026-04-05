'''Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be inserted in order.
leetcode no : 35 '''

# Search Insert position

def Insert_position(nums,target):
    left = 0
    right = len(nums) - 1

    while left <= right :
        mid = (left+right) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
print(Insert_position([1,2,3,4,5,6,7,8],6))
print(Insert_position([1,3,5,6],2))