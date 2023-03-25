from collections import Counter 
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def solve():
     n = int(input())
     arr = IL()
     ans = []
     i = 0
     while i < len(arr)-1:
          temp = float("-inf")
          while i < (len(arr)-1) and arr[i]*arr[i+1] > 0:
               temp = max(temp,arr[i])
               i += 1
          if temp != float("-inf"):
               ans.append(max(temp,arr[i]))
          else:
               ans.append(arr[i])
          i += 1
     if ans and  ans[-1]*arr[-1] < 0:
          ans.append(arr[-1])
     if ans :
          print(sum(ans))
     if not ans:
          print(arr[0])
          
T = I()
for ___ in range(T):
     solve()