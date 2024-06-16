class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        added,miss,i = 0,1,0
        while  miss <= n:
            if i < len(nums) and miss >= nums[i]:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                added += 1
        return added