# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        count = 0
        def bfs(root):
            nonlocal count
            que = deque([(root,root.val)])
            ans = []
            while que:
                node,curr_sum = que.popleft()
                if curr_sum == targetSum: count += 1
                if node.left:
                    left = node.left
                    left_sum = curr_sum + left.val
                    que.append((left,left_sum))
                if node.right:
                    right = node.right
                    right_sum = curr_sum + right.val
                    que.append((right,right_sum))
                # print(que)
        def dfs(root):
            if not root:
                return 
            else:
                bfs(root)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return count