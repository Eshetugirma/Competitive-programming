class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #===>>> declare important variables
        rows = len(mat)
        cols = len(mat[0])
        que = deque()
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        #==>>> traverse all grid and add to que zero positions
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]:
                    mat[i][j] = "#"
                else:
                    que.append((i,j))
        #===>>> for all zero positions find distance from all non zero positions
        while que:
            i,j = que.popleft()
            
            for (x,y) in directions:
                row,col = i+x, j+y

                if 0 <= row < rows and 0 <= col < cols and mat[row][col] == "#":
                    mat[row][col] = mat[i][j] + 1
                    que.append((row,col))
        return mat