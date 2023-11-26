from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # graph = {}
        graph = defaultdict(defaultdict)
        n = len(equations)
        for i in range(n):
            e1, e2 = equations[i]
            val = values[i]
            for e in [e1, e2]:
                if e not in graph:
                    graph[e] = defaultdict(float)
            graph[e1][e2] = val
            graph[e2][e1] = 1 / val

        res = []
        for i in range(len(queries)):
            denom, nom = queries[i]
            if denom not in graph or nom not in graph: 
                res.append(-1)
            else:
                tmp = self.bfs(graph, denom, nom)
                res.append(tmp)
        return res

    def bfs(self, graph, src, target):
        que = deque([src])
        ret = 1
        visited = {src: ret}
        while que:
            now = que.popleft()
            if now == target:
                ret = visited[now]
                # break
                return ret
            for nbr in graph[now].keys():
                ratio = graph[now][nbr]
                if nbr not in visited:
                    new_quotient = visited[now] * ratio
                    que.append(nbr)
                    visited[nbr] = new_quotient
        # return ret
        return -1  