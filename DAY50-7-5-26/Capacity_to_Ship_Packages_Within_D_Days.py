'''PROBLEM : Capacity to Ship Packages Within D Days
LeetCode 1011
Problem: Given weights of packages and days d, return the minimum ship capacity to deliver all packages within d days.
Approach: Binary search on capacity range [max(weights), sum(weights)]. Greedy check for feasibility.
Time: O(n log(sum(weights))) | Space: O(1)'''

def shipWithinDays(weights, d):
    def can(cap):
        days, curr = 1, 0
        for w in weights:
            if curr + w > cap:
                days += 1
                curr = 0
            curr += w
        return days <= d

    low, high = max(weights), sum(weights)
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if can(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


# --- TEST ---
print(shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))  # Expected: 15
print(shipWithinDays([3,2,2,4,1,4], 3))           # Expected: 6
print(shipWithinDays([1,2,3,1,1], 4))             # Expected: 3
