class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #===>>>> declare the visited set 
        visited = set()
        #===>>> do dfs on every row
        def dfs(row):
            visited.add(row)
            for col in range(len(isConnected)):
                if isConnected[row][col] and col not in visited :
                    dfs(col)
        count = 0
        for row in range(len(isConnected)):
            if row not in visited :
                dfs(row)
                count += 1

        return count