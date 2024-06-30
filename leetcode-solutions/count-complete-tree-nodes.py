# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def left(node):
            nonlocal depth
            if not node:
                return 
            depth += 1
            left(node.left) 
            left(node.right)
        depth = 0
        left(root)
        return depth
        


        
