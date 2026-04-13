class Solution3:
    def unionSortedArrays(self, arr1: list[int], arr2: list[int]) -> list[int]:
        i, j = 0, 0
        result = []

        while i < len(arr1) and j < len(arr2):
            print(f"Comparing arr1[{i}]={arr1[i]} and arr2[{j}]={arr2[j]}")
            if i > 0 and arr1[i] == arr1[i - 1]:
                print(f"Skipping duplicate in arr1: {arr1[i]}")
                i += 1
                continue
            if arr1[i] <= arr2[j]:
                if not result or result[-1] != arr1[i]:
                    result.append(arr1[i])
                    print(f"Added {arr1[i]} from arr1 → {result}")
                i += 1
            else:
                if not result or result[-1] != arr2[j]:
                    result.append(arr2[j])
                    print(f"Added {arr2[j]} from arr2 → {result}")
                j += 1

        while i < len(arr1):
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
                print(f"Added remaining {arr1[i]} from arr1 → {result}")
            i += 1

        while j < len(arr2):
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
                print(f"Added remaining {arr2[j]} from arr2 → {result}")
            j += 1

        print("Final union result:", result)
        return result


# Example usage
arr1 = [1, 2, 2, 3, 5]
arr2 = [2, 3, 4, 5, 6]
print("Array 1:", arr1)
print("Array 2:", arr2)
result = Solution3().unionSortedArrays(arr1, arr2)
print("Union:", result)