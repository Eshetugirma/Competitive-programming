# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def helper(root,path,pathlist):
            if not root:
                return

            if not root.left and not root.right:

                path += str(root.val)
                pathlist.append(path)

                path = ""
            path += str(root.val) + "->"

            helper(root.left,path,pathlist)
            helper(root.right,path,pathlist)
            return pathlist
            
        return helper(root,"",[])