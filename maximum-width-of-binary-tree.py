# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic = defaultdict(list)
        def order(level,root,temp=1):

            if not root:
                return 
            #==>>>> append your identifier at the same level
            dic[level].append(temp)
            #===>>>> give your identifier for left double of before and for right double plus one
            order(level+1,root.left,temp*2)
            order(level+1,root.right,temp*2+1)
            return
        order(0,root)
        list_of_list = list(dic.values())
        ans = 1
        for stack in list_of_list:
            ans = max(ans,stack[-1]- stack[0]+1)

        return ans