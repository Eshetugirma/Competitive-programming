class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        
        queens = {(i, j) for i, j in queens}
        
        for i in [-1, 0, 1]:
           
            for j in [-1, 0, 1]:
                for k in range(1, 8):
                    x, y = king[0] + i * k, king[1] + j * k
                    if (x, y) in queens:
                        ans.append([x, y])
                        break
        return ans