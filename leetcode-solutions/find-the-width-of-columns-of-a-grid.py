class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        target = [0]*len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                target[j] = max(target[j],len(str(grid[i][j])))
        return target
        