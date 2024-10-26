class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        take, not_take = 0, 0
        memo = Counter(nums)
        for i in range(max(nums), min(nums) - 1, -1):
            take_current = not_take + i*memo[i]
            not_take = max(take, not_take)
            take = take_current
        return max(take, not_take)



        