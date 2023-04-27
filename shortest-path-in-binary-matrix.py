class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        temp = deque()
        path_length = 1

        if not grid[0][0] and len(grid)==1:
            return 1
        if (grid[0][0] or grid[len(grid)-1][len(grid)-1]):
            return -1
        else:
            visited.add((0,0)) 
            queue.append((0,0))

        while queue:
            i,j = queue.popleft()
            
            directions = ((0,1),(1,1),(1,0),(0,-1),(-1,0),(-1,-1),(-1,1),(1,-1))
            added = 0
            for (x,y) in directions:

                row, col = i+x,j+y
                if not (0 <= row < len(grid) and 0 <= col < len(grid)) or grid[row][col] or (row,col) in visited:
                    continue
                if row == col == len(grid)-1:
                    return path_length+1
                visited.add((row,col))
                temp.append((row,col))
            if not queue:
                queue = temp
                temp = deque()
                path_length += 1
        
            


            
        return -1