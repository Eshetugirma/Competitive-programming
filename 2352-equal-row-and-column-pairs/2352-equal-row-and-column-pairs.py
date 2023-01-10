class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # by using builtin function of transpose
        tpse = Counter(zip(*grid))       # <-- determine the transpose and hash the rows
        
        grid = Counter(map(tuple,grid))  # <-- hash the rows of grid. (Note the tuple-map, so
                                         #     we can compare apples w/ apples in next step.)
            
        return  sum(tpse[t]*grid[t] for t in tpse)