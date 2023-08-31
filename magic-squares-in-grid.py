class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        for x in range(1,len(grid)-1):
            for y in range(1,len(grid[0])-1):
                # sum of diagonals
                diagonal1 = grid[x][y] + grid[x+1][y+1] + grid[x-1][y-1]
                diagonal2 = grid[x][y] + grid[x-1][y+1] + grid[x+1][y-1]
                # sum of rows
                row1 = grid[x][y] + grid[x][y-1] + grid[x][y+1]
                row2 = grid[x-1][y] + grid[x-1][y-1] + grid[x-1][y+1]
                row3 = grid[x+1][y] + grid[x+1][y-1] + grid[x+1][y+1]
                # sum of columns
                col1 = grid[x][y] + grid[x+1][y] + grid[x-1][y]
                col2 = grid[x][y-1] + grid[x+1][y-1] + grid[x-1][y-1]
                col3 = grid[x][y+1] + grid[x+1][y+1] + grid[x-1][y+1]
                # checker for distinctness
                check = sorted([grid[x][y], grid[x][y-1], grid[x][y+1], grid[x-1][y], grid[x-1][y-1], grid[x-1][y+1], grid[x+1][y], grid[x+1][y-1], grid[x+1][y+1]])
                # print(check)
                if diagonal1==diagonal2==row1==row2==row3==col1==col2==col3 and check == [1,2,3,4,5,6,7,8,9]:
                    count += 1
        return count