class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        
        seen = set()
        digit = set(['0','1','2','3','4','5','6','7','8','9'])
        curr = []
        for char in word:
            if char in digit:
                curr.append(char)
            else:
                if curr:
                    num = int(''.join(curr))
                    seen.add(num)
                    curr = []
        if curr:
            num = int(''.join(curr))
            seen.add(num)
        return len(seen)
                