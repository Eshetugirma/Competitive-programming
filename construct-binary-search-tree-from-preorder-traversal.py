# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        dummy = root
        for num in preorder[1:]:
            curr = TreeNode(num)
            if stack[-1].val > num:
                stack[-1].left = curr
                stack.append(curr)
                continue
            temp = stack[-1]
            while stack and stack[-1].val < num:
                temp = stack.pop()
            temp.right = curr
            stack.append(curr)
        return dummy