class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        for i in nums:
            if dic[i]==1:
                return i