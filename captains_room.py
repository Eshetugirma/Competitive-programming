# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
rooms = map(int, input().split())
mydict = {}
for i in rooms:
    if i not in mydict:
        mydict[i] = 0
    mydict[i] += 1
for key, values in mydict.items():
    if mydict[key] == 1:
        print(key)
