class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        def baundary(x,y): return 0 <= x < len(grid2) and 0 <= y < len(grid2[0])
        def bfs(visited,que,flag):
            while que:
                (i,j) = que.popleft()
                for (x,y) in directions:
                    row,col = x+i,y+j
                    if (row,col) not in visited and baundary(row,col) and grid2[row][col]:
                        if not grid1[row][col]:
                            flag = False
                        que.append((row,col))
                        visited.add((row,col))
            return flag

        visited = set()
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid1[i][j] and grid2[i][j] and (i,j) not in visited:
                    visited.add((i,j))
                    que = deque()
                    que.append((i,j))
                    if bfs(visited,que,True):
                        count += 1
        return count