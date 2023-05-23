# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x      
#         self.left = None
#         self.right = None  
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:return [target.val]
        graph = defaultdict(list)
        que = deque([root])
        while que:
            length = len(que)
            for i in range(length):
                node = que.popleft()
                if node.left:
                    graph[node].append(node.left)
                    graph[node.left].append(node)
                    que.append(node.left)
                if node.right:
                    graph[node].append(node.right)
                    graph[node.right].append(node)
                    que.append(node.right)
        que = deque([target])
        visited = {target}
        level = 0
        ans = []
        while que:
            length = len(que)
            for i in range(length):
                currNode = que.popleft()
                if level == k:
                    ans.append(currNode.val)
                else:
                    for nextNode in graph[currNode]:
                        if nextNode not in visited:
                            visited.add(nextNode)
                            que.append(nextNode)
            level += 1
        return ans