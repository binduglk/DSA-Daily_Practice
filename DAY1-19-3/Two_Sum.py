# You have a list of numbers and a target number. Find two numbers in the list that add up to the target. 
# Return their positions (index numbers). There is always exactly one answer.
# nums = [2, 7, 11, 15], target = 9 Answer: [0, 1] because nums[0]+nums[1] = 2+7 = 9 
# nums = [3, 2, 4], target = 6 Answer: [1, 2] because nums[1]+nums[2] = 2+4 = 6

def two_sum(nums,target): 
    seen = {}   # stores num which are visited , its indexes

    for i, num in enumerate(nums): # enumerate gives like (index,positionvalue)(0,2)
        diff = target - num

        if diff in seen: # IF WE ALReady SEEN THAT NUM
            return [seen[diff],i]
        
        seen[num] = i # if we not yet visited

    return[]

print(two_sum([2, 7, 11, 15], 9)) 
print(two_sum([3, 2, 4], 6))       
print(two_sum([3, 3], 6))

