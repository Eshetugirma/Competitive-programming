class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        #==>>> construct graph by reversing 
        for i in range(len(edges)):
            graph[edges[i][1]].append(edges[i][0])
        #==>>>> this is the bfs function which called for all nodes separetly 
        def bfs(que,temp,visited):
            while que:
                curr = que.popleft()
                for el in graph[curr]:
                    if el not in visited:
                        visited.add(el)
                        que.append(el)
                        temp.append(el)
            temp.sort()
            return temp
        
        ans = []
        #==>>> here I call bfs for every node to know whom are his ancestors
        for i in range(n):
            if graph[i]:
                ans.append(bfs(deque(graph[i]),graph[i],set(graph[i])))
                pass
            else:
                ans.append([])
        return ans