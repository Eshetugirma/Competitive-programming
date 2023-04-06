from collections import Counter 
from collections import defaultdict
from bisect import bisect_left,bisect_right
def testcase(): return int(input())
def maps(): return map(int, input().split())
def lists(): return list(map(int, input().split()))
def sorts(): return sorted(map(int, input().split()))
def solve():
     l,r = maps()
     print(l) if l == r else print(1)
T = 1
for ___ in range(T):
   solve()