class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origin = image[sr][sc]
        def backtracking(i,j):
            
            # this to check the boundary and the see if the position is color then return to back
            if not (0 <= i < len(image)  and  0 <= j < len(image[0])) or image[i][j] != origin:
                return
            image[i][j] = color
            backtracking(i-1,j)
            backtracking(i+1,j) 
            backtracking(i,j-1)
            backtracking(i,j+1)
        if image[sr][sc] != color: 
            backtracking(sr,sc)
        return image
# class Solution(object):
#     def floodFill(self, image, sr, sc, newColor):
#         rows, cols, orig_color = len(image), len(image[0]), image[sr][sc]
#         def traverse(row, col):
#             if (not (0 <= row < rows and 0 <= col < cols)) or image[row][col] != orig_color:
#                 return
#             image[row][col] = newColor
#             [traverse(row + x, col + y) for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0))]
#         if orig_color != newColor:
#             traverse(sr, sc)
#         return image