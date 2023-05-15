# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        total = float('-inf')
        def dfs(root):
            nonlocal total
            if not root:
                return 0
            left = max(0,dfs(root.left))
            right = max(0,dfs(root.right))
            total = max(total,left+right+root.val)
            return max(right,left)+root.val
        dfs(root)
        return total