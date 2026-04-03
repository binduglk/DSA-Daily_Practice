# Session 3 - Symmetric Tree
# LeetCode #101
# Topic - Tree Comparison
# Day 13

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(left, right):
            # both None → symmetric
            if not left and not right:
                return True
            # one None → not symmetric
            if not left or not right:
                return False
            # values must match and children must be mirrors
            return (left.val == right.val and
                    isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))

        return isMirror(root.left, root.right)

# Testing

# Symmetric tree:
#     1
#    / \
#   2   2
#  /\   /\
# 3  4 4  3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

sol = Solution()
print(sol.isSymmetric(root))    # True

# Not symmetric:
#     1
#    / \
#   2   2
#    \   \
#    3    3
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(3)

print(sol.isSymmetric(root2))   # Falses