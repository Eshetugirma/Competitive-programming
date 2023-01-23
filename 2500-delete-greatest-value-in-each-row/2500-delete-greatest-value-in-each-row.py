class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        # ==>> sort all rows in grid 
        for row in range(len(grid)):
            grid[row].sort()
        # ==>> iterate all columns to pop maximum element in rows
        for col in range(len(grid[0])):
            maxima = 0
            # ==>> collect maximum from all rows
            for row in range(len(grid)):
                temp = grid[row].pop() 
                maxima = max(maxima,temp)
            ans += int(maxima)
        # ==>> here to return the sum of all maximum in each rows
        return ans 