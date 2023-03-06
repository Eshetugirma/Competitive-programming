t = int(input())
for i in range(t):
     a,b = map(int, input().split())
     left = 0
     right = min(a,b)
     while left < right:
          mid = (left+right)//2
          if mid >= (a+b)//4:
               right = mid
          else:
               left = mid+1
     print(right)
