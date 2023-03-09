class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        def backtrack(visited,temp):

            if len(temp) == len(nums):
                ans.append(temp[::])
                return 
            for i in nums:
                if i in visited:
                    continue
                else:
                    temp.append(i)
                    visited.add(i)
                    backtrack(visited,temp)
                    temp.pop()
                    visited.remove(i)
            return 

        backtrack(set(),[])
        return ans