class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def backtracking(i,curr,count):
            if count == 4 and i == len(s):
                ans.append(curr[:-1])
                return 
            if count > 4 :
                return 
            for j in range(i,min(i+3,len(s))):
                if int(s[i:j+1]) <= 255  and (len(s[i:j+1]) == 1 or s[i] != "0"):
                    backtracking(j+1,curr+s[i:j+1]+".",count+1)
        backtracking(0,"",0)
        return ans