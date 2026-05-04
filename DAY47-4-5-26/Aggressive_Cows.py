'''PROBLEM : Aggressive Cows (Binary Search on Answer)
Classic Problem (Binary Search on Answer)
Problem: Place cows in stalls such that the minimum distance between any two cows is maximized.
Approach: Binary search on distance. Check feasibility with greedy placement.
Time: O(n log(max_distance)) | Space: O(1)'''

def canPlace(stalls, cows, dist):
    count = 1
    last = stalls[0]
    for i in range(1, len(stalls)):
        if stalls[i] - last >= dist:
            count += 1
            last = stalls[i]
            if count == cows:
                return True
    return False


def aggressiveCows(stalls, cows):
    stalls.sort()
    left, right = 1, stalls[-1] - stalls[0]
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if canPlace(stalls, cows, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


# --- TEST ---
print(aggressiveCows([1,2,4,8,9], 3))  # Expected: 3
print(aggressiveCows([1,2,3,4,5], 2))  # Expected: 4
