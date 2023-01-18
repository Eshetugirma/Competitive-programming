class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # this is user friendly solution for this problem
        for i in range(9):
            seen = set()
            for j in range(9):
                curr = board[i][j]
                if curr == '.':
                    continue
                if curr in seen:
                    return False
                seen.add(curr)
        for j in range(9):
            seen = set()
            for i in range(9):
                curr = board[i][j]
                if curr == '.':
                    continue
                if curr in seen:
                    return False
                seen.add(curr)
        for i in range(3):
            for j in range(3):
                seen = set()
                for r in range(i*3,i*3+3):
                    for c in range(j*3,j*3+3):
                        curr = board[r][c]
                        if curr == '.':
                            continue
                        if curr in seen:
                            return False
                        seen.add(curr)
        return True

# this is the modefied one 
'''class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        box = collections.defaultdict(set)
        for row in range(9):  #length of board is == 9
            for col in range(9):
                if board[row][col]=='.':
                    continue
                if (board[row][col] in rows[row] or 
                    board[row][col] in cols[col] or 
                    board[row][col] in box[row//3,col//3]):
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                box[row//3,col//3].add(board[row][col])
        return True'''