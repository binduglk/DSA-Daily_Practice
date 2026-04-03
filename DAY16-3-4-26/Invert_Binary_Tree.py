# Session 2 - Invert Binary Tree
# LeetCode #226
# Topic - Tree Traversal
# Day 13

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        # swap left and right
        root.left, root.right = root.right, root.left
        # recurse on children
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Helper to print tree in preorder
def preorder(node):
    if not node:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)

# Testing
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

sol = Solution()
inverted = sol.invertTree(root)

print("Preorder of inverted tree:", preorder(inverted))