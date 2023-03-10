# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:        
        def merged(root1,root2):
            if root1 and root2:
                node = TreeNode(root2.val + root1.val)
                node.left = merged(root1.left,root2.left)
                node.right = merged(root1.right,root2.right)
                return node
            return root1 or root2
        return merged(root1, root2)