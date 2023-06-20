class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(1,1),(1,-1),(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1)]


        def dfs(board, row ,col):
            if board[row][col] != "E":
                return
            count = 0
            for i, j in directions:
                r, c = row + i, col + j
                if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == "M":
                    count += 1
            if count:
                board[row][col] = str(count)
            else:
                board[row][col] = "B"
                for i, j in directions:
                    r, c = row + i, col + j
                    if 0 <= r < len(board) and 0 <= c < len(board[0]):
                        dfs(board, r, c)
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X" 
        else:
            dfs(board, click[0], click[1])
        return board