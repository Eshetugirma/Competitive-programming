class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig = int("".join(map(str,digits)))
        dig =  list(str(dig+1))
        for i in range(len(dig)):
            dig[i] = int(dig[i])

            
        return dig