class Solution:
    def getRow(self, rowIndex: int) -> List[int]:


        memo = [ [0]*(rowIndex+1) for i in range(rowIndex+1) ]

        def helper(i,j):

            if not i or not j or i==j:
                return 1

            if not memo[i][j]: 
                
                memo[i][j] = helper(i-1,j-1)+ helper(i-1,j)


            return memo[i][j]

        ans = []

        for i in range(rowIndex+1):

            ans.append(helper(rowIndex,i))

        return ans
