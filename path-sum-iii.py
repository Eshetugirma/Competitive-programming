# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val 
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1
        def dfs(node,curr):
            count = 0
            if not node:
                return 0
            curr += node.val
            count = sums[curr-targetSum] 
            sums[curr] += 1
            count += dfs(node.left,curr ) + dfs(node.right,curr)
            sums[curr] -= 1
            return count 
        return dfs(root,0)