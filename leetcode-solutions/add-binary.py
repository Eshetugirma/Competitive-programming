class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if int(a)+int(b) == 0 :return "0"
        a = '0'*(10**4-len(a)) + a
        b = '0'*(10**4-len(b)) + b
        answer = ['0']*10**4
        carry = 0
        
        for i in range(10**4-1,-1,-1):
            current = int(a[i]) + int(b[i])
            if current == 2 and carry :
                answer[i] ='1'
            elif current == 2 and not carry or current == 1 and carry:
                carry = 1
            else:
                answer[i] = str(current + carry)
                carry = 0
        # print(answer)
        res = ''.join(answer)
        res = res.lstrip('0')
        return res