class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            start = 2
            while start*start <= num:
                while not num%start:
                    dic[start] = 1
                    num //= start
                if start == 2:
                    start += 1
                else:
                    start += 2
            if num != 1:
                dic[num] = 1
        return len(dic)