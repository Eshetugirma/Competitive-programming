# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal ans,count 
            count = left + right
            if root.val == p.val or root.val == q.val:
                count += 1
            if count == 2:
                count = 3
                ans = root
            return count
        ans,count = root, 0
        dfs(root)
        return ans