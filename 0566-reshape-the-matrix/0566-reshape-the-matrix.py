class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        output = [[0 for i in range(c)] for i in range(r)]
        idx = 0
        while idx < r * c:
            output[idx // c][ idx % c] =  mat[idx // len(mat[0])][idx % len(mat[0])]
            idx += 1
        return output