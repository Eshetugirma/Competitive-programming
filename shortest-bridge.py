class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        directions = ((0,1),(-1,0),(0,-1),(1,0))
        def check(r,c): return c < 0 or r < 0 or n == r or n == c
        def dfs(i,j):
            if (i,j) in visited or check(i,j) or not grid[i][j]:
                return 
            visited.add((i,j))
            for (x,y) in directions:
                r,c = x+i,y+j
                dfs(r,c)

        def bfs(ans,que):
            while que:
                length = len(que)
                for _ in range(length):
                    i,j = que.popleft()

                    for (x,y) in directions:
                        r,c = x+i,y+j
                        if (r,c) in visited or check(r,c):
                            continue
                        if grid[r][c]:
                            return ans
                        visited.add((r,c))
                        que.append((r,c))
                ans += 1
                        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    dfs(i,j)
                    return bfs(0,deque(visited))