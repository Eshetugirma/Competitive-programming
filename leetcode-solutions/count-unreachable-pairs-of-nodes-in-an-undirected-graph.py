class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        seen = set()
        def bfs(i):
            que = deque([i])
            seen.add(i)
            temp = 1

            while que:

                for i in range(len(que)):
                    currNode = que.popleft()
                    for newNode in graph[currNode]:

                        if newNode not in seen:
                            seen.add(newNode)
                            que.append(newNode)
                            temp += 1
            return (n-temp)*temp
        total = 0
        for i in range(n):
            if i not in seen:
                total += bfs(i)
        return total//2


