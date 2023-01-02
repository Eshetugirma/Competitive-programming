class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mydict = {}
        for i in range(len(nums)):
            mydict[nums[i]] = i
        for i in range(1,len(nums)+1):
            if i not in mydict:
                return i
            
        return 0