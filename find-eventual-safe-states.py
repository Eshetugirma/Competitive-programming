class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        connections = defaultdict(list)
        degree = defaultdict(int)
        for i in range(len(graph)):
            degree[i] += len(graph[i])
            for el in graph[i]:
                connections[el].append(i)
        ans = [i for i in range(len(graph)) if degree[i] == 0]
        que = deque(ans)
        while que:
            temp = que.popleft()
            for i in connections[temp]:
                degree[i] -= 1
                if not degree[i]:
                    ans.append(i)
                    que.append(i)
        ans.sort()
        return ans