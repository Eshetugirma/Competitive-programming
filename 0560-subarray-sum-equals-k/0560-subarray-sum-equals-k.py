class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        summ = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        #==>>> every itaretion check if sum is in prefix sum before and add count
        for i in nums:
            summ += i
            diff = summ - k
            count += prefix_sum[diff]
            prefix_sum[summ] += 1
        return count