class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = defaultdict()
        rank = defaultdict()
        for i in range(n):
            parent[i] = i
            rank[i] = 1
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        def union(x,y):
            u = find(x)
            v = find(y)
            if u==v: return 
            if rank[u] >= rank[v]:
                parent[v] = u
                rank[u] += 1
            else:
                parent[u] = v
                rank[v] += 1
        for edge in edges:
            union(edge[0],edge[1])
        return find(source) == find(destination)