class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(index,prevVal):
            #==>>> this is my base case if my index is became lenght return true
            if index==len(s):
                return True
            #===>>> itarete for all element after taken ones to check
            for j in range(index,len(s)):
                val=int(s[index:j+1])
                if prevVal <= val:
                    return 
                if prevVal-val==1 and dfs(j+1,val):
                    return True
            return False
        for i in range(len(s)-1):
            val=int(s[:i+1])
            if dfs(i+1,val):
                return True
        return False