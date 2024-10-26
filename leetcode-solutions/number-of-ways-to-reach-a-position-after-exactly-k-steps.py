class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        startPos += k
        endPos += k
        memo = [[-1,0] for i in range(startPos + endPos+2)]
        memo[startPos] = [0,1]
        for i in range(k):

            for j in range(1,len(memo)-1):

                if memo[j][0] == i:
                    if memo[j-1][0] == i + 1:
                        memo[j-1][1] += memo[j][1] 

                    else:
                        memo[j-1][0],memo[j-1][1] = memo[j][0]+1,memo[j][1]
                        

                    if memo[j+1][0] == i + 1:
                        memo[j+1][1] += memo[j][1] 

                    else:
                        memo[j+1][0],memo[j+1][1] = memo[j][0]+1,memo[j][1]

        # print(memo)
        return memo[endPos][1]% (10**9 + 7) if memo[endPos][0] == k else 0



