# Given a list of numbers, return True if any number appears more than once. 
# Return False if all numbers are unique.
# Input : [1, 2, 3, 1] → True (1 appears twice) Input : [1, 2, 3, 4] → False (all unique) 
# Input : [1, 1, 1, 3, 3] → True (1 and 3 repeat)

def duplicate(nums):
    seen = set() # contains the visited number , empty

    for num in nums:
        if num in seen:
            return True # if num is in seen 
        seen.add(num) # not seen yet add it
    return False 

print(duplicate([1,2,3,4,1]))
print(duplicate([6,7,5,4,8,9]))
