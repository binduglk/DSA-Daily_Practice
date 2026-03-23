'''Given an array and integer k, find the subarray of length k with the maximum average. 
Return that average.
nums=[1,12,-5,-6,50,3], k=4 → 12.75 Subarray [12,-5,-6,50] sum=51, avg=51/4=12.75 
nums=[5], k=1 → 5.0'''

def max_avg_arr(nums,k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k,len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i-k]

        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum / k

print(max_avg_arr([1,12,-5,-6,50,3], 4)) 
print(max_avg_arr([5], 1)) 