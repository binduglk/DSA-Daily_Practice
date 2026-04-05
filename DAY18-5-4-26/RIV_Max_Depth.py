# Session 1 - Maximum Depth of Binary Tree
# LeetCode #104
# Topic - DFS Recursion
# Day 13

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # base case
        if not root:
            return 0

        # recursive case
        left_depth  = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)

# Testing
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print(sol.maxDepth(root))    # 3
print(sol.maxDepth(None))    # 0