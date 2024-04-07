class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        def check(row,col):
            if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0 or grid[row][col] == 0:
                return 0
            else:
                return 1
        def bfs(x,y):
            que = deque([(x,y)])
            visited.add((x,y))
            perimeter = 0
            while que:
                x,y = que.popleft()
                for (i,j) in [(0,1),(1,0),(-1,0),(0,-1)]:
                    row,col = x+i,y+j
                    if check(row,col) :
                        if (row,col) not in visited:
                            que.append((row,col))
                            visited.add((row,col))
                    else:
                        perimeter += 1
            return perimeter
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    return bfs(row,col)

