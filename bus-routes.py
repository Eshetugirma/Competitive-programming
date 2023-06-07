class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:return 0
        routes = list(map(set,routes))
        graph = defaultdict(set)
        visited,targets = set(),set()
        que = deque()
        for i in range(len(routes)):
            if source in routes[i]:
                visited.add(i)
                que.append((i,1))
            if target in routes[i]:
                targets.add(i) 
                
            for j in range(i+1,len(routes)):
                if routes[i] & routes[j]:
                    graph[i].add(j)
                    graph[j].add(i)
        while que:
            prev,level = que.popleft()
            if prev in targets: return level
            for curr in graph[prev]:
                if curr in visited: continue
                visited.add(curr)
                que.append((curr,level+1))
        return -1