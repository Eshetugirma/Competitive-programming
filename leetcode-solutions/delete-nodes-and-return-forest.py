# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        forest = []
        def dfs(root):
            if root.left:
                root.left = dfs(root.left)
            if root.right:
                root.right = dfs(root.right)
            if root.val in to_delete:
                if root.left:
                    forest.append(root.left)
                if root.right:
                    forest.append(root.right)
                return None
            return root
        if dfs(root):
            forest.append(root)
        return forest