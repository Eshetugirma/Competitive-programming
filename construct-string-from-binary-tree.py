# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(root):
            ans = str(root.val)
            if root.left:
                ans += "(" + dfs(root.left) + ")"
            if root.right:
                if not root.left :
                    ans += "()"
                ans += "(" + dfs(root.right) + ")"
            return ans
        return dfs(root)