# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        val = 0
        def tree(node):
            nonlocal val
            if node:
                tree(node.right)
                val += node.val
                node.val = val
                tree(node.left)
            return node
        return tree(root)

        