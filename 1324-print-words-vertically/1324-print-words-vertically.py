class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        ans = []
        mux_len = 0
        for word in words:
            mux_len = max(len(word),mux_len)
        for i in range(mux_len):
            temp = ""
            for word in words:
                if len(word)>i:
                    temp += word[i]
                else: 
                    temp += " "
                    
            t_string = temp.rstrip()
            ans.append(t_string)
                    
        return ans
                
                
                