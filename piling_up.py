# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
testcase = int(input())

for i in range(testcase):
    n, cubes = input(), deque(map(int, input().split()))
    we_can = "Yes"
    vertical = float('inf')
    while len(cubes) > 1:
        
        left = cubes.popleft()
        
        right = cubes.pop()
        
        if left >= right and left <= vertical:
             vertical = left
             
             cubes.append(right)
        
        elif right > left and right <= vertical:
            vertical = right
            
            cubes.appendleft(left)
        
        else:
            we_can = "No"
            break
    print(we_can)
