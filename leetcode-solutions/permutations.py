class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtracking(temp,visited):
            if len(temp) == n:
                ans.append(temp[::])
                return
            for i in nums:
                print(i,)
                if (i) not in visited:
                    visited.add(i)
                    temp.append(i)
                    backtracking(temp,visited)
                    temp.pop()
                    visited.remove(i)
        backtracking([],set())
        return ans


        