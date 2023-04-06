class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        n = 2**len(nums)
        for i in range(n):
            check = 0
            for j in range(len(nums)):
                if (i >> j) & 1:
                    check |= nums[j]
            dic[check] += 1
        mx = max(dic)
        return dic[mx]