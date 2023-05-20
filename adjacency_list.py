from collections import Counter 
from collections import defaultdict
from bisect import bisect_left,bisect_right
from math import lcm
def testcase(): return int(input())
def maps(): return map(int, input().split())
def lists(): return list(map(int, input().split()))
def sorts(): return sorted(map(int, input().split()))
def solve():
   n = testcase()
   grid = [lists() for i in range(n)]
   for i in range(n):
      visited = []
      for j in range(n):
         if grid[i][j]:
               visited.append(j+1)
      print(len(visited),*visited)
T = 1
for ___ in range(T):
   solve()