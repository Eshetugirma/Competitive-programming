# Enter your code here. Read input from STDIN. Print output to STDOUT
num_e = int(input())
stud_e = set(input().split())
num_f = int(input())
stud_f = set(input().split())

print(len(stud_e.difference(stud_f)))
