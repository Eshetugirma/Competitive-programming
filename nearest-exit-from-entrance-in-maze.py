class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        #===>>> declare important variables
        rows = len(maze)
        cols = len(maze[0])
        que = deque()
        directions = ((0,-1),(0,1),(1,0),(-1,0))
        que.append((entrance[0],entrance[1],0))
        #==>>>> we dont need to use extra space for visited just we can change "." to "+" 
        maze[entrance[0]][entrance[1]] = "+"
        while que:
            x,y,distance = que.popleft() 
            #==>> if see possible exit the return the distance it have from entrance
            if (0 in [x,y] or x == rows-1 or y == cols-1) and [x,y] != [entrance[0],entrance[1]]:
                return distance 
            #===>>>> find new possible pass from neighbors of the cell
            for (i,j) in directions:

                row,col = x+i,y+j 
                #===>>>> if get new possible way append to que and then mark it visited or impossible pass
                if 0 <= row < rows and 0 <= col < cols and maze[row][col] == ".":
                    maze[row][col] = "+"
                    que.append((row,col,distance+1))
        return -1