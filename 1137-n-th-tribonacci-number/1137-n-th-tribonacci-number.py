class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1
        tn = 0
        for i in range(n-2):
            tn = t0 + t1 +t2
            t0 = t1
            t1 = t2
            t2 = tn
        return t2 if n!=0 else t0
        