'''You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is built upon the previous one, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''

# Mock implementation for local testing
def isBadVersion(version: int) -> bool:
    bad = 4   # let's assume version 4 is the first bad one
    return version >= bad


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                # mid is bad → the first bad could be at mid or earlier
                right = mid
            else:
                # mid is good → the first bad must be after mid
                left = mid + 1

        # when left == right, we've found the first bad version
        return left


# Test locally
print(Solution().firstBadVersion(5))  # Output: 4