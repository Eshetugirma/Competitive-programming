# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p and q:
            return False
        if not q and p:
            return False
        #==>>> check all elements of both by traversing simultaneously
        left = self.isSameTree(q.left,p.left)*(q.val == p.val)
        right = self.isSameTree(q.right,p.right)*(q.val == p.val)
        return left*right