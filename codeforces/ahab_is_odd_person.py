n = int(input())
a = list(map(int, input().split()))
odd = False
even = False
for x in a:
   if x % 2 == 0:
        even = True
   else:
        odd = True
if odd==even:
     a.sort()
print(*a)
