class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # steps 1
        # declare the memory variable and boundary checking function 
        memo = [ [True]*len(grid[0]) for _ in range(len(grid))]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        total_island = 0

        # step 2
        # implement checking and bfs functions
        def checking(r,c): return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        def bfs(i,j):
            que = deque([(i,j)])
            while que:
                r,c = que.popleft()
                # print(grid,que)/
                for x,y in directions:
                    new_r , new_c = x+r, y + c
                    
                    
                    if checking(new_r,new_c) and grid[new_r][new_c] == '1':
                        # print(grid[new_r][new_c])
                        # print(r,c , "and ", new_r,new_c)
                        # print(grid)
                        # memo[y+r][y+c] = False
                        grid[new_r][new_c] = '0'
                        que.append((new_r,new_c))
            
        # step 3
        # write itaretive loop to check every island and call bfs functions
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    total_island += 1
                    bfs(i,j)
        # step 4
        # return answer and run after analysing the code
        return total_island