class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        def backtrack(visited,temp):
            #==>>> copy every formed permutation
            if len(temp) == len(nums):
                ans.append(temp[::])
                return               
            for i in range(len(nums)):
                #==>>> if element at index is already used pass over it 
                if (visited & (1 << i)):
                    continue
                #==>>> append element at index and make it visited
                temp.append(nums[i])
                visited |= 1 << i
                backtrack(visited,temp)
                #===>>>> after used pop temp and delete from visited
                temp.pop()
                visited &= ~( 1 << i ) 
        backtrack(0,[])
        return ans