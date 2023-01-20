from collections import Counter
n,m = map(int,input().split())
grid = [list(input()) for i in range(n)]
columns = [Counter([ grid[i][j] for i in range(m) ] ) for j in range(n)]
rows = [Counter(grid[i]) for i in range(n)]
ans = ""
for row in range(n):
     for col in range(m):
          if (rows[row][grid[row][col]]<2 and columns[col][grid[row][col]]<2):
               ans += (grid[row][col])
print(ans)
