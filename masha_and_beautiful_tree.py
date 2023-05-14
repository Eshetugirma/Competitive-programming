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
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] -= 1
    z = 0
    while len(a) > 1:
        b = []
        for i in range(0, len(a), 2):
            if a[i] // 2 != a[i + 1] // 2:
                z = -1e9
            if a[i] > a[i + 1]:
                z += 1
            b.append(a[i] // 2)
        a = b
    if z < 0:
        z = -1
    print(z)


T = testcase()
for ___ in range(T):
   solve()

