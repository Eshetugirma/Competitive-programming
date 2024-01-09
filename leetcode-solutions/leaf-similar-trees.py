# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def leaf(root,ans):
            if not root:
                return
            elif root and not root.left and not root.right:
                ans.append(root.val)
            leaf(root.left,ans)
            leaf(root.right,ans)
            return ans
 
        return leaf(root1,[]) == leaf(root2,[])