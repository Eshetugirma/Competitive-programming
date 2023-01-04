class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = []
        index = 0
        while index < len(s):
            
            if index + 2 < len(s) and s[index + 2] == "#":
                
                ans.append(chr(96+int(s[index:index+2])))
                index += 3
            else:
                ans.append(chr(96+int(s[index])))
                index += 1
               
        return "".join(ans)