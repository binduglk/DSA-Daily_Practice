'''Every number in the array appears exactly twice except one number which appears only once. 
Find that number.
Input : [2, 2, 1] → Output: 1 Input : [4, 1, 2, 1, 2] → Output: 4 
Input : [1] → Output: 1'''

def singlenum(nums):
    seen = set()

    for num in nums:
        if num in seen:
            seen.remove(num) # seen twice removes it 
        else:
            seen.add(num)  # first time then add it 
    
    return seen.pop() # returns unique num 

print(singlenum([1,2,3,1,3]))
