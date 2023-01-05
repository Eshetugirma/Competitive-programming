# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
na,nb = map(int,input().split())
a,b=defaultdict(list),[]
for i in range(na):
    a[input()].append(i+1) 
for i in range(nb):
    b.append(input())

for i in range(nb): 
    if(a[b[i]]):
        print(' '.join(map(str,a[b[i]])))
    else:
        print("-1")
