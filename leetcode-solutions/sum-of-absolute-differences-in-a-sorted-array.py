class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefx_sum,ans = [0],[]
        for i in range(len(nums)):
            prefx_sum.append(prefx_sum[i]+nums[i])
        for i in range(len(nums)):
            left = (i+1)*nums[i] - prefx_sum[i+1]
            right = prefx_sum[-1] - prefx_sum[i] - (len(nums)-i)*nums[i]
            ans.append(right+left)
        return ans


        