class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ans = 0
        freq = defaultdict(int)
        for x in deliciousness: 
            for k in range(22): ans += freq[2**k - x]
            freq[x] += 1
        return ans % 1_000_000_007

'''
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = 0
        n = len(deliciousness)
        for left in range(n):
            right = left + 1
            while right < n:
                sums = deliciousness[left] + deliciousness[right]
                if (math.ceil(log2(sums)) == math.floor(log2(sums))):
                    count += 1
                right += 1
        return count%1_000_000_007
        '''