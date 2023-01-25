# ==>>> here is my codeforce submisssion link >>>https://codeforces.com/problemset/submission/1399/190484080
t = int(input())
for testcase in range(t):
     n = int(input())
     a = list(map(int,input().split()))
     a.sort()
     right = 1
     left = 0
     while right<len(a):
          if a[right]-a[left] <=1:
               a.remove(a[left])
          else:
               print("NO")
               break
     if len(a) <=1 :
          print("YES")
