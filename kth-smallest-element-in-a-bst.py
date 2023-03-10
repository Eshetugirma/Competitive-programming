# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #===>>> traverse on root inorder traversal which is sorted list
        def small(root):
            if not root:
                return []
            ans = small(root.left)
            ans.append(root.val)
            ans.extend(small(root.right))
            return ans
        res = small(root)
        #===>>> from sorted list return k indexed element
        return res[k-1]