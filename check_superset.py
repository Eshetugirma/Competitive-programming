# Enter your code here. Read input from STDIN. Print output to STDOUT
super_set = list(map(int,input().split()))
n = int(input())
my_checker = []
for i in range(n):
      
    if all ((i in super_set for i in list(map(int,input().split())))):
        my_checker.append(True)
    else:
            my_checker.append(False)
print(all(my_checker))
            
        
