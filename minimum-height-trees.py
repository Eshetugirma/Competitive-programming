class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        if n == 1: return [0]
        if n == 2: return [0,1]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])


        que = deque()
        for i in range(n):
            if len(graph[i]) == 1:
                que.append(i)


        nodes = n
        while nodes > 2:
            nodes -= len(que)

            for i in range(len(que)):
                leaf = que.popleft()
                temp = graph[leaf][0]
                graph[temp].remove(leaf)

                if len(graph[temp]) == 1:
                    que.append(temp)
                    
        return list(que)