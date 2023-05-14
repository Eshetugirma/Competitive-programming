# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #===>>>> find all path and hold them in lists
        def findpath(root,path,stack):
            if not root:
                return
            if not root.left and not root.right:
                path += str(root.val)
                stack.append(path)
                path = ""
            path += str(root.val)
            findpath(root.left,path,stack)
            findpath(root.right,path,stack)
            return stack
        lists = findpath(root,"",[])
        #===>>>> sum all path in list 
        ans = 0
        for i in lists:
            ans += int(i)
        return ans