# ---- Problem 2: Left Rotate by 1 ----
# Topic - Array Manipulation

class Solution2:
    def rotateByOne(self, arr: list[int]) -> list[int]:
        print(f"Original array: {arr}")
        temp = arr[0]   # store first element
        for i in range(1, len(arr)):
            arr[i - 1] = arr[i]
            print(f"Step {i}: shifted arr[{i}]={arr[i]} to arr[{i-1}] → {arr}")
        arr[-1] = temp
        print(f"Placed first element {temp} at the end → {arr}")
        return arr


# Testing
nums = [1, 2, 3, 4, 5]
sol = Solution2()
rotated = sol.rotateByOne(nums)
print("Final rotated array:", rotated)