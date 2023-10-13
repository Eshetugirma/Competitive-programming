# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,mn,mx):
            if not root:
                return True
            if (mn >= root.val or mx <= root.val):
                return False
            left = dfs(root.left,mn,root.val)
            right = dfs(root.right,root.val,mx)

            return left*right

        return dfs(root,float('-inf'),float('inf'))