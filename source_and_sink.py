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
   grid = []
   sink = [0]*n
   source = [0]*n
   for i in range(n):
      grid.append(list(map(int, input().split())))
   for row in range(n):
      for col in range(n):
         if grid[row][col] == 1:
            source[row] = 1
            sink[col] = 1
   sources = []
   sinks = []
   for i in range(n):
      if not sink[i] and not source[i]:
         sink[i] = 1
         source[i] = 1
      elif sink[i] and source[i]:
         sink[i] = 0
         source[i] = 0
      if sink[i]:
         sinks.append(i+1)
      if source[i]:
         sources.append(i+1)
   print(len(sources),*sources)
   print(len(sinks),*sinks)
T = 1
for ___ in range(T):
   solve()