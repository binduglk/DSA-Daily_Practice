# Session 3 - Replace Words
# LeetCode #648
# Topic - Trie
# Day 19

class TrieNode:
    def __init__(self):   # corrected
        self.children = {}
        self.is_end = False

class Solution:
    def replaceWords(self,
                     dictionary: list,
                     sentence: str) -> str:

        # Build Trie
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True

        # Replace words
        def findRoot(word):
            node = root
            prefix = ""
            for char in word:
                if char not in node.children:
                    return word    # no root found
                node = node.children[char]
                prefix += char
                if node.is_end:
                    return prefix  # root found
            return word

        words = sentence.split()
        return " ".join(findRoot(w) for w in words)

# Testing
sol = Solution()
print(sol.replaceWords(
    ["cat","bat","rat"],
    "the cattle was rattled by the battery"))
# "the cat was rat by the bat"

print(sol.replaceWords(
    ["a","b","c"],
    "aadsfasf absbs bbab cadsfafs"))
# "a a b c"