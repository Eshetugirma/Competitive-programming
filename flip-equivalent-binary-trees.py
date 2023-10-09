# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2: return True
        elif not root1 and root2 or not root2 and root1: return False
        elif root1.val != root2.val: return False

        def check(left1,right1,left2,right2):
            if left1 == left2 and right1 == right2:
                return (True,False)
            elif left1 == right2 and left2 == right1:
                return (True,True)
            else:
                return (False,False)
        def dfs(root1,root2):
            if root1.left: left1 = root1.left.val
            else: left1 = -1

            if root1.right: right1 = root1.right.val
            else: right1 = -1

            if root2.left: left2 = root2.left.val
            else: left2 = -1

            if root2.right: right2 = root2.right.val
            else: right2 = -1
            
            correct,flip = check(left1,right1,left2,right2)

            if not correct: return False

            if flip:
                if root1.right and root2.left:
                    if not dfs(root1.right,root2.left):
                        return False
                    

                if root1.left and root2.right:
                    if not dfs(root1.left,root2.right):
                        return False

                
            else:
                 
                 if root1.left and root2.left:
                    if not dfs(root1.left,root2.left):
                        return False


                 if root1.right and root2.right:
                    if not dfs(root1.right,root2.right):
                        return False
                        
            return True 

        return dfs(root1,root2)