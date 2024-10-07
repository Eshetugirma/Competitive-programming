class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        mn_len = inf
        for s in strs:
            mn_len = min(mn_len,len(s))


        for i in range(mn_len):
            yes = 0

            for j in range(len(strs)-1):

                if strs[j][i] == strs[j+1][i]:
                    yes += 1
                else:
                    return strs[0][:i]

        return strs[0][:mn_len]



                
        print(mn_len)
        return ""