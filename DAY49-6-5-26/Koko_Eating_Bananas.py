'''PROBLEM : Koko Eating Bananas
LeetCode 875
Problem: Koko loves bananas. Given piles of bananas and h hours, find the minimum eating speed k such that all bananas are eaten within h hours.
Approach: Binary search on eating speed. Compute hours needed at each speed.
Time: O(n log(max(pile))) | Space: O(1)'''

import math

def minEatingSpeed(piles, h):
    low, high = 1, max(piles)
    ans = high

    while low <= high:
        mid = (low + high) // 2
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / mid)

        if hours <= h:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


# --- TEST ---
print(minEatingSpeed([3,6,7,11], 8))   # Expected: 4
print(minEatingSpeed([30,11,23,4,20], 5))  # Expected: 30
print(minEatingSpeed([30,11,23,4,20], 6))  # Expected: 23
