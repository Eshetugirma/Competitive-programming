class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = defaultdict()
        rank = defaultdict()
        
        for i in range(1,len(edges)+1):
            parent[i] = i
            rank[i] = 0
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x
        for edge in edges:
            u = find(edge[0])
            v = find(edge[1])
            if v==u: return edge
            if rank[v] >= rank[u]:
                parent[u] = v
                rank[v] += rank[u]
            else:
                parent[v] = u
                rank[u] += rank[v]