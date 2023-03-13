class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(i,temp):
            if i > n+1:
                return
            if len(temp) == k:
                ans.append(temp[::])
                return 
            temp.append(i)
            backtrack(i+1,temp)
            temp.pop()
            backtrack(i+1,temp)

        backtrack(1,[])
        return ans