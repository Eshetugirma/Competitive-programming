class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        que = deque([0])

        seen = set(restricted)
        seen.add(0)
        count = 1
        while que:
            curr = que.popleft()
            for child in graph[curr]:
                if child not in seen:
                    # print(child)
                    count += 1
                    seen.add(child)
                    que.append(child)
        return count