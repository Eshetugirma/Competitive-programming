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
   m = testcase()
   dic = defaultdict(list)
   for i in range(m):
      temp = lists()
      if temp[0] == 1:
         dic[temp[1]].append(temp[2])
         dic[temp[2]].append(temp[1])
      else:
         print(*dic[temp[1]])
T = 1
for ___ in range(T):
   solve()