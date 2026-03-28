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
