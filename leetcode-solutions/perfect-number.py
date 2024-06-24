class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        count = 0
        n = int(sqrt(num))
        for i in range(1,n+1):
            
            if not num%i and num > (num//i) > n:
                # print(num,i,count)
                count += (i + num//i)
            elif not num%i:
                count += i
        # print(count)
        return num == count if n!=1 else False