class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(set)
        for x,y in dislikes:
            adj[x].add(y)
            adj[y].add(x)
        self.visited = {}
        self.invalid = False
        def dfs(node):
            if self.invalid:
                return
            
            if node not in self.visited:
                self.visited[node] = 0
            
            for n in adj[node]:
                if n not in self.visited:
                    self.visited[n] = self.visited[node] + 1
                    dfs(n)
                elif (self.visited[n] - self.visited[node]) %2 == 0:
                    self.invalid = True
                    return
        for i in range(1, n+1):
            dfs(i)
            if self.invalid:
                return False
        
        return True