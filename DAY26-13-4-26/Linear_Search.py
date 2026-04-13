class Solution2:
    def linearSearch(self, arr: list[int], target: int) -> int:
        for i in range(len(arr)):
            print(f"Checking index {i}: value = {arr[i]}")
            if arr[i] == target:
                print(f"Target {target} found at index {i}")
                return i
        print(f"Target {target} not found in the list")
        return -1


# Example usage
arr = [10, 20, 30, 40, 50]
target = 30
print("Array:", arr)
print("Target:", target)
result = Solution2().linearSearch(arr, target)
print("Search result index:", result)