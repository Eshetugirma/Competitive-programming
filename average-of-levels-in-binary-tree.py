# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        average = []
        def bfs(queue):
            average.append(sum([d.val for d in queue])/len(queue))
            temp = deque()
            while queue:
                rot = queue.popleft()
                if rot.left:
                    temp.append(rot.left)
                if rot.right:
                    temp.append(rot.right)
            if temp:
                bfs(temp)
        bfs(queue)
        return average