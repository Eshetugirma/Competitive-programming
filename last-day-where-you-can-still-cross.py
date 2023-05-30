class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        directions = ((0,1),(1,0),(0,-1),(-1,0))
        grid = [[1]*col for _ in range(row)]
        parent = [i for i in range(row*col+2)]
        rank = [ 1 for _ in range(row*col+2)]
        def find(x):
            if x == parent[x]:
                return x
            return find(parent[x])
        def union(x,y):
            rep1 = find(x)
            rep2 = find(y)
            if rank[rep1] > rank[rep2]:
                rep1,rep2 = rep2,rep1
            parent[rep1] = rep2
            rank[rep2] = rank[rep1]
        for i in range(len(cells)-1,-1,-1):
            r,c = cells[i][0]-1,cells[i][1]-1
            grid[r][c] = 0
            index_1 = r*col+c+1
            for dr ,dc in directions:
                newr,newc = r+dr,c+dc
                index_2 = newr*col+newc+1
                if 0 <= newr < row and 0 <= newc < col and grid[newr][newc] == 0:
                    union(index_1,index_2)
            if r == 0:
                union(0,index_1)
            if row-1 == r:
                union(row*col+1,index_1)
            if find(0) == find(row*col+1):
                return i