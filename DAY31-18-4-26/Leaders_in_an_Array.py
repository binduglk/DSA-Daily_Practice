# PROBLEM 22: Leaders in an Array
# (Classic Array Problem — not directly on LeetCode, but often asked)
# Question: An element is a leader if it is greater than or equal to all elements to its right.
# Return all leaders in the array in left-to-right order.
# ============================================================

class Solution22:
    def leaders(self, arr: list[int]) -> list[int]:
        result = []
        max_from_right = float('-inf')

        print("Initial max_from_right = -inf")

        # scan right to left
        for i in range(len(arr) - 1, -1, -1):
            print(f"Index={i}, Value={arr[i]}, Current max_from_right={max_from_right}")
            if arr[i] >= max_from_right:
                result.append(arr[i])               # current is a leader
                max_from_right = arr[i]             # update running max
                print(f"   Leader found: {arr[i]}, Updated max_from_right={max_from_right}")
            else:
                print(f"   Not a leader")

        result.reverse()                            # restore left-to-right order
        print("Final leaders (left-to-right):", result)
        return result

# Testing
sol = Solution22()
print("Answer:", sol.leaders([16,17,4,3,5,2]))   # Expected [17,5,2]
print("Answer:", sol.leaders([1,2,3,4,0]))       # Expected [4,0]
print("Answer:", sol.leaders([7,10,4,10,6,5,2])) # Expected [10,10,6,5,2]
