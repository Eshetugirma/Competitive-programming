# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return 

        que = deque([(root,root.val,[root.val])])
        ans = []
        while que:
            node,curr_sum,path = que.popleft()
            if node.left:
                left = node.left
                left_sum = curr_sum + left.val
                left_path = path + [left.val]
                que.append((left,left_sum,left_path))
            if node.right:
                right = node.right
                right_sum = curr_sum + right.val
                right_path = path + [right.val]
                que.append((right,right_sum,right_path))
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    ans.append(path)
            # print(que)
        return ans