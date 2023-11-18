class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sets = set(nums)
        for i in range(len(nums)):
            curr = target - nums[i] 
            if curr != nums[i] and curr in sets:
                # print(nums[i])
                return [i,nums.index(curr)]
            elif curr in sets:
                temp = [i,nums.index(curr)]
                
        return temp