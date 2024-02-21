class Solution:
    def smallestNumber(self, num: int) -> int:
        # check parity
        parity = 1
        if num < 0:
            parity = 0
            num *= -1
        
        stack = [0]*10
        # count the digit and order them
        for n in str(num):
            stack[int(n)] += 1
        # destribute the ordered elements and return depending on their parity
        ans = ""
        for i in range(1,10):
            ans += stack[i]*str(i)

        if not ans:
            return 0
        elif not parity:
            return - int(ans[::-1] + stack[0]*str(0))
        return int(ans[0]+stack[0]*str(0)+ans[1:])
        
        