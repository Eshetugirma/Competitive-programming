# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        #==>>> hold elements in dic by their columns position 
        def traverse(root,row=0,col=0):
            if not root:
                return 
            dic[col].append([row,root.val])
            traverse(root.left,row+1,col-1)
            traverse(root.right,row+1,col+1)
        traverse(root)
        result = []
        #===>>>> sort by column and then by row 
        for x in sorted(dic.keys()):
            column = [i[1] for i in sorted(dic[x])]
            result.append(column)

        return result