class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def check(r,c): return 1 <= r < n-1 and 1 <= c < m-1
        seen = set()
        count = 0
        def bfs(que,i,j):
            temp = 0
            que.append((i,j))
            seen.add((i,j))
            while que:
                
                length = len(que)
                r,c = que.popleft()

                for x,y in directions:
                    print(que,i,j)
                    row,col = x+r,y+c
                    if check(row,col) and grid[row][col] == 0 and (row,col) not in seen:
                        seen.add((row,col))
                        que.append((row,col))
                    elif not grid[row][col] and (row,col) not in seen:
                        temp += 1
                
            return not temp

        for i in range(1,n-1):
            for j in range(1,m-1):
                if (i,j) not in seen and not grid[i][j]:
                    count += int(bfs(deque(),i,j))
        return count