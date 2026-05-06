'''PROBLEM : Book Allocation
GFG (Binary Search on Answer)
Problem: Allocate books to m students such that the maximum number of pages assigned to a student is minimized. Each student must get at least one book, and books are allocated contiguously.
Approach: Binary search on the maximum pages. Check feasibility with greedy allocation.
Time: O(n log(sum(pages))) | Space: O(1)'''

def is_possible(pages, n, m, max_pages):
    students = 1
    current = 0
    for i in range(n):
        if current + pages[i] <= max_pages:
            current += pages[i]
        else:
            students += 1
            current = pages[i]
            if students > m:
                return False
    return True


def findPages(pages, n, m):
    if m > n:
        return -1

    low, high = max(pages), sum(pages)
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if is_possible(pages, n, m, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


# --- TEST ---
print(findPages([12,34,67,90], 4, 2))  # Expected: 113
print(findPages([5,17,100,11], 4, 4))  # Expected: 100
