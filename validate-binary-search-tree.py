# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(root):
            if not root:
                return []
            res = check(root.left)
            res.append(root.val)
            res.extend(check(root.right))
            return res

        array = check(root)
        if len(array) == 1:
            return True

        for i in range(1, len(array)):
            if array[i-1] >= array[i]:
                return False

        return True