class Solution:
    def reverse(self, x: int) -> int:
        count = 0
        if x<0:
            count += 1
            x = abs(x)
        s = str(x)
        reverse = s[::-1]
        if int(reverse)<-(pow(2,31)) or int(reverse)>=pow(2,31):
            return 0
        
        return (int(reverse)) if count == 0 else -1*int(reverse)
        