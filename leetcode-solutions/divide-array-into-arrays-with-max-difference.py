class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        start = nums[0]
        for i in range(0,len(nums)-2,3):
            # print(i,ans)
            if nums[i+2] - nums[i] <= k:
                ans.append(nums[i:i+3])
            else: return []
        return ans
        