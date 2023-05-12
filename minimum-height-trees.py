class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        #==>>> if n is one or two then they are already equal length
        if n == 1: return [0]
        if n == 2: return [0,1]
        #===>>> create the graph
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])


        que = deque()
        #==>>> find all leave at first
        for i in range(n):
            if len(graph[i]) == 1:
                que.append(i)


        nodes = n
        #==>>  do topological sort by bfs
        while nodes > 2:
            nodes -= len(que)

            for i in range(len(que)):
                leaf = que.popleft()
                temp = graph[leaf][0]
                graph[temp].remove(leaf)

                if len(graph[temp]) == 1:
                    que.append(temp)

        return list(que)