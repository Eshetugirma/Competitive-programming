# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            if not root.val%2:
                ans += childofchild(root,0)
            dfs(root.left)
            dfs(root.right)
        def childofchild(node,sons):
            if node.left and node.left.left:
                sons += node.left.left.val
            if node.left and node.left.right:
                sons += node.left.right.val
            if node.right and node.right.left:
                sons += node.right.left.val
            if node.right and node.right.right:
                sons += node.right.right.val
            return sons
        dfs(root)
        return ans