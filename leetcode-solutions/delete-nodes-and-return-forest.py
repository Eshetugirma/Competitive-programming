# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left 
#         self.right = right 
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        toDelete = set(to_delete)
        remainingForest = []

        def deleteTree(root):
            
            if root.left:
                root.left = deleteTree(root.left)
            if root.right:
                root.right = deleteTree(root.right)
            if root.val in toDelete:
                if root.left:
                    remainingForest.append(root.left)
                if root.right:
                    remainingForest.append(root.right)
                return None
            return root

        if deleteTree(root):
            remainingForest.append(root)
        return remainingForest

