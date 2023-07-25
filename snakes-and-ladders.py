class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        for i in range(1,len(board),2): board[i].reverse()
        arr = [0] + list(chain(*board))
        que = deque([1])
        seen = {1}
        level = 0
        while que:
            for _ in range(len(que)):
                curr = que.popleft()
                if curr == len(arr)-1: return level

                for i in range(curr+1,min(curr+7,len(arr))):
                    nxt = arr[i] if arr[i] != -1 else i
                    if nxt not in seen:
                        que.append(nxt)
                        seen.add(nxt)
            level += 1
        
        return -1