class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if not n: return 0

        nums = [0,1]
        for i in range(2,n+1):
            if i%2:
                nums.append(nums[i//2] + nums[i//2+1])
            else:
                nums.append(nums[i//2])
        return max(nums)