# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #==>>> declare dictionary to add every elements in the same level to list
        dic = defaultdict(list)
        def order(level,root):
            if not root:
                return 
            #===>>>> append element at the same level
            dic[level].append(root.val)
            #==>>>> call element at every level
            order(level+1,root.left)
            order(level+1,root.right)
            return
        order(0,root)
        ans = []
        lists = list(dic.values())
        #==>>> from every level append element at the right most position to our answer
        for i in lists:
            ans.append(i[-1])
        return ans