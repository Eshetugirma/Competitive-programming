class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = bank[0].count('1')
        for i in range(1,len(bank)):
            curr = bank[i].count('1')
            # print(curr,prev)
            if not curr: continue
            ans += prev*curr
            prev = curr
        return ans
            
        