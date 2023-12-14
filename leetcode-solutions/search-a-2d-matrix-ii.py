class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix[0])):
            left, right = 0, len(matrix)
            while left < right:
                
                md = (left + right)//2 
                if matrix[md][i] > target:
                    right = md
                elif matrix[md][i] < target:
                    left = md+1
                else: return True

        return False
        