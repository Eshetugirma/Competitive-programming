class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        directions = [(0,-1,'L'), (0,1,'R'), (-1,0,'T'), (1,0,'B')]
        check = { 
            (1,'R'): (1,3,5),
            (1,'L'): (1,4,6),
            (2,'T'): (2,3,4),
            (2,'B'): (2,5,6),
            (3,'L'): (1,4,6),
            (3,'B'): (2,5,6),
            (4,'R'): (1,3,5),
            (4,'B'): (2,5,6),
            (5,'L'): (1,4,6),
            (5,'T'): (2,3,4),
            (6,'T'): (2,3,4),
            (6,'R'): (1,3,5), }
        seen = {(0,0)}
        def inBoundary(i,j): return 0 <= i < n and 0 <= j < m and (i,j) not in seen
        def bfs(que,i,j):
            que.append((i,j))
            row,col = i,j
            while que:
                row,col = que.pop()
                for x,y,d in directions:
                    newR,newC = row+x,col+y
                    if inBoundary(newR,newC) and (grid[row][col],d) in check and grid[newR][newC] in check[(grid[row][col],d)]:
                        que.append((newR,newC))
                        seen.add((newR,newC))
                    else:
                        if row == n-1 and col == m-1:
                            return True 
            return False

        return bfs(deque(),0,0)