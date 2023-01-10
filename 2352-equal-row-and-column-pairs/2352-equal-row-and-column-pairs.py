class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid2= []
        count = 0
        
        
        for i in range(len(grid[0])):
            grid2.append([])
            for row in grid:
                grid2[i].append(row[i])
                
        for row in grid:
            
            for column in grid2:
                
                if str(row) == str(column):
                    
                    count += 1
            
        return count