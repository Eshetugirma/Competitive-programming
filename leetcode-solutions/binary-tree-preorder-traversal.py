# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def tree(root):
            if not root:
                return
            ans.append(root.val)
            if not root.right and root.left:
                tree(root.left)
            elif root.right and not root.left:
                tree(root.right)
            elif root.right and root.left:
                tree(root.left)
                tree(root.right)
        tree(root)
        return ans
                
        