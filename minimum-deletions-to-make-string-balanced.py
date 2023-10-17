class Solution:
    def minimumDeletions(self, s: str) -> int:
        curr_a, curr_b = 0,0
        total_a = s.count('a')
        total_b = len(s) - total_a
        ans = float('inf')
        b = 0
        for c in s:
            
            curr_a += (c=='a')
            curr_b += (c=='b')
            if (c=='b'): b = 1
            ans = min(ans,curr_b + (total_a-curr_a - b))
            b = 0
            
            print(ans)
        return ans