class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origin = image[sr][sc]
        def backtracking(i,j):
            
            # this to check the boundary and the see if the position is color then return to back
            if not (0 <= i < len(image)  and  0 <= j < len(image[0])) or image[i][j] != origin:
                return
            image[i][j] = color
            [backtracking(i+x,j+y) for (x,y) in (( 0,1), (1,0), (-1,0), (0,-1))]
        if image[sr][sc] != color: 
            backtracking(sr,sc)
        return image