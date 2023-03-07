# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        backward = root.right
        forward = root.left
        def check(r,l):
            if not r and not l:
                return True
            if not r and l:
                return False
            if not l and r:
                return False
            #==>>> check for every branch of tree 
            right = check(r.left,l.right)*(r.val == l.val)
            left = check(r.right,l.left)*(r.val == l.val)
            return right*left
        return check(forward,backward)