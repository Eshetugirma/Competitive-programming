class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        temp = sorted(nums)
        ans = []
        for i in range(len(nums)):
            if temp[i] == target:
                ans.append(i)
        return ans