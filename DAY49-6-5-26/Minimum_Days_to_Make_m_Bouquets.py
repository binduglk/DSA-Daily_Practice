'''PROBLEM : Minimum Days to Make m Bouquets
LeetCode 1482
Problem: Given an array bloomDay, an integer m (bouquets), and k (flowers per bouquet), return the minimum number of days needed to make m bouquets. If impossible, return -1.
Approach: Binary search on days. Check feasibility by scanning bloomDay.
Time: O(n log(max(bloomDay))) | Space: O(1)'''

def can_make(bloomDay, m, k, day):
    bouquets, flowers = 0, 0
    for bloom in bloomDay:
        if bloom <= day:
            flowers += 1
            if flowers == k:
                bouquets += 1
                flowers = 0
        else:
            flowers = 0
    return bouquets >= m


def minDays(bloomDay, m, k):
    if m * k > len(bloomDay):
        return -1

    low, high = min(bloomDay), max(bloomDay)
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if can_make(bloomDay, m, k, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


# --- TEST ---
print(minDays([1,10,3,10,2], 3, 1))   # Expected: 3
print(minDays([1,10,3,10,2], 3, 2))   # Expected: -1
print(minDays([7,7,7,7,12,7,7], 2, 3)) # Expected: 12
