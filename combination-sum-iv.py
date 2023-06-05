class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        memo[0] = 1
        for i in range(1,target+1):
            memo[i] = 0
            for num in nums:
                memo[i] += memo[i-num]
        return memo[target]