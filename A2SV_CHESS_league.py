from collections import Counter 
from collections import defaultdict
from bisect import bisect_left,bisect_right
from math import lcm
def testcase(): return int(input())
def maps(): return map(int, input().split())
def lists(): return list(map(int, input().split()))
def sorts(): return sorted(map(int, input().split()))
def solve():
    n, k = maps()
    nums = lists()
    def mergeSort(left, right):
        if left >= right:
            return [(left, nums[left])]
        mid = (left + right) // 2
        left_arr = mergeSort(left, mid)
        right_arr = mergeSort(mid + 1, right)
        return merge(left_arr, right_arr)
    def merge(l_arr, r_arr):
        arr = []
        p1 = 0
        p2 = 0
        
        while p1 < len(l_arr) and p2 < len(r_arr):
            if  l_arr[p1][1] < (r_arr[p2][1] - k):
                p1 += 1
            elif r_arr[p2][1] < (l_arr[p1][1] - k):
                p2 += 1
            else:
                break
        i = 0
        total = (len(l_arr) - p1) + (len(r_arr) - p2)
        while i < total:
            if p1 < len(l_arr) and (p2 >= len(r_arr) or l_arr[p1][1] <= r_arr[p2][1]):
                arr.append(l_arr[p1])
                p1 += 1
            else:
                arr.append(r_arr[p2])
                p2 += 1
            i += 1
        return arr
    ans = sorted(mergeSort(0, len(nums) - 1))
    res = []
    for a in ans:
        res.append(a[0]+1)
    print(*res)

T = 1
for ___ in range(T):
   solve()

