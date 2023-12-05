class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        que = deque([[0]])
        ans = []
        while que:
            curr = que.popleft()
            if curr[-1] == len(graph)-1:
                ans.append(curr)
            else:
                for num in graph[curr[-1]]:
                    que.append(curr+[num])
        return ans
