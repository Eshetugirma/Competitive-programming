class Solution:
    def minimumSum(self, num: int) -> int:
        # ==>> this is the simplest way
        nums = sorted(str(num),reverse=True)
        return int(nums[3]+nums[0]) + int(nums[2] + nums[1])
        