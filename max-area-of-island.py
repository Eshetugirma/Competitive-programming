class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(i,j):
            nonlocal count
            if not ( 0 <= i < len(grid) and 0 <= j < len(grid[0]) ) or grid[i][j] == 0 or (i,j) in visited:
                return 0 
            visited.add((i,j))
            count += 1
            [dfs(i+x,j+y) for (x,y) in ((1,0),(0,1), (-1,0), (0,-1))]
            return count
        stack = []
        for i in range(len(grid)):

            for j in range(len(grid[0])):
                count = 0
                if grid[i][j] == 1:
                    stack.append(dfs(i,j))
        return max(stack) if stack else 0