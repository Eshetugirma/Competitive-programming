class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        ans = 0
        prefix_sum = 0
        dic[0] = 1
        # in every iteration use reminder of prefix sum by k 
        for num in nums:
            prefix_sum += num
            rem = prefix_sum%k 
            # add reminder count to answer as subarray sum divided by k
            ans += dic[rem]
            dic[rem] += 1
        return ans