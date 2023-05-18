class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = defaultdict()
        rank = defaultdict()
        
        for i in range(1,n+1):
            parent[i] = i
            rank[i] = 0
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
            
        for edge in roads:
            u = find(edge[0])
            v = find(edge[1])
            if v==u: continue
            if rank[v] >= rank[u]:
                parent[u] = v
                rank[v] += rank[u]
            else:
                parent[v] = u
                rank[u] += rank[v]
        ans = float("inf")
        target = find(1)
        for edge in roads:
            if target == find(edge[0]):
                ans = min(ans,edge[2])
        return ans