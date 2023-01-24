#codeforce_link==>>https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/submission/190422995
n,m = map(int,input().split())
n_list = list(map(int,input().split()))
m_list = list(map(int,input().split()))
pointer1 = 0 
pointer2 = 0
ans = []
while len(ans) != m:
     if pointer1 >= n:
          ans.append(n)
     elif n_list[pointer1] >= m_list[pointer2]:
          ans.append(pointer1)
          pointer2 +=1
     else:
          pointer1 +=1
print(*ans)
