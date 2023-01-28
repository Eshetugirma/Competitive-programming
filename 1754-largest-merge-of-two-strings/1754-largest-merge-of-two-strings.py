class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:  
                                                      
        w1, w2, ans = list(word1), list(word2),''
        while w1 and w2:                                
            ans+= w1.pop(0) if w1 > w2 else w2.pop(0)   
        return  ans + ''.join(w1) + ''.join(w2)  