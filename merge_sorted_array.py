,m = map(int,input().split())
n_list = list(map(int,input().split()))
m_list = list(map(int,input().split()))
point1 = 0 
point2 = 0
ans = []
for i in range(n+m):
     if point1 < n and point2 < m:
          if n_list[point1] <= m_list[point2]:
               ans.append(n_list[point1])
               point1 +=1
          else:
               ans.append(m_list[point2])
               point2 += 1
     elif point1 >= n:
          ans.append(m_list[point2])
          point2 +=1
     elif point2 >= m:
          ans.append(n_list[point1])
          point1 +=1
print(*ans)
