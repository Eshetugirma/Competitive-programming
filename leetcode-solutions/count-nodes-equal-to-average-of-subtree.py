# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            nonlocal count
            if not node:
                return 0,0
            leftTree = dfs(node.left)
            rightTree = dfs(node.right)

            currentSum = leftTree[0] + rightTree[0] + node.val
            numberOfNode = leftTree[1] + rightTree[1] + 1
            if currentSum//numberOfNode == node.val:
                count += 1
            return currentSum,numberOfNode
        count = 0
        dfs(root)
        return count