class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        def find(row,col):
            if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0 or grid[row][col] == 0:
                return 1
            if (row,col) in visited:
                return 0 
            visited.add((row,col))
            ans = find(row,col+1)
            ans += find(row,col-1)
            ans += find(row+1,col)
            ans += find(row-1,col)
            return ans
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    return find(row,col)