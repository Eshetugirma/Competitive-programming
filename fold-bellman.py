from collections import *    
from bisect import *
from heapq import *   
import sys

def take_input():
    return sys.stdin.readline().rstrip('\n')

def take_int_input():
    return int(take_input())

def take_list_input():
    return list(map(int, take_input().split()))


def testcase(): return int(input())
def maps(): return map(int, input().split())
def lists(): return list(map(str, input().split()))
def sorts(): return sorted(map(int, input().split()))
def solve():
    n,m = take_list_input()
    arr = [1e9]*n
    arr[0] = 0
    edges = []
    for i in range(m):
        a,b,c = take_list_input()
        edges.append((a-1,b-1,c))

    for _ in range(n-1):
        for edge in edges:
            u, v, w = edge
            if arr[u] != 1e9 and arr[u] + w < arr[v]:
                arr[v] = arr[u] + w
    
    for i in range(len(arr)):
        if arr[i] == 1e9:
            arr[i] = 30000
    print(*arr)
T = 1
for _ in range(T):
   solve()