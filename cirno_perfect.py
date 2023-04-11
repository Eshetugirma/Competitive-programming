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
   count = 0
   bit = list(bin(n)[2:][::-1])
   index = bit.index('1')
   for i in bit:
      count += int(i)
   if count > 1:
      print(2**index)
   elif index == 0:
      print(3)
   else:
      print(2**index+1)
T = testcase()
for ___ in range(T):
   solve()