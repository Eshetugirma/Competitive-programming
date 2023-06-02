# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(root,check):
            if not root:
                return 0
            takeL = 0
            takeR = 0
            notTakeL = 0
            notTakeR = 0
            if (root,check) in memo:
                return memo[(root,check)]
            if check:
                takeL = dp(root.left,False)
                takeR = dp(root.right,False)
            notTakeL = dp(root.left,True)
            notTakeR = dp(root.right,True)
            if check:
                memo[(root,check)] = max(root.val+takeL+takeR,notTakeR+notTakeL)
                return memo[(root,check)]
            return notTakeR+notTakeL
        return dp(root,True)