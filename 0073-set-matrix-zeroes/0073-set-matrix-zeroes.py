class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        dic = {}
        key = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    dic[key] = [row,col]
                    key += 1
        for ind in range(len(dic)):
            x,y = map(int,dic[ind])
            for row in range(len(matrix)):
                matrix[row][y] = 0
            for col in range(len(matrix[0])):
                matrix[x][col] = 0
        return matrix
                