class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_move = 0
        n = len(nums)
        for i in range(n):
            max_move = max(max_move,nums[i])
            if max_move == 0 and i < n-1:
                return False
            max_move -= 1
        return True