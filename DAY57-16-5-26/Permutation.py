class Solution:
    def findPermutation(self, s):
        result = []

        def backtrack(path, remaining):
            if not remaining:
                result.append(path)
                return

            used = set()

            for i in range(len(remaining)):
                if remaining[i] in used:
                    continue

                used.add(remaining[i])

                backtrack(
                    path + remaining[i],
                    remaining[:i] + remaining[i+1:]
                )

        backtrack("", s)

        return sorted(result)