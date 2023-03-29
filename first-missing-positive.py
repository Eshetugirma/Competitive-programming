class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] > len(nums) or nums[i] < 0:
                nums[i] = 0
            dic[nums[i]] = 1
        if 0 in dic:
            del dic[0] 
        if not dic:
            return 1 
        for i in range(len(nums)+1):
            if i+1 not in dic:
                return i+1