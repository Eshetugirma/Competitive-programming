class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        stack = []
        temp = sorted(nums)
       
        my_dict = {}
        for i in range(len(temp)):
            if temp[i] not in my_dict:
                my_dict[temp[i]] = i
        for i in nums:
            stack.append(my_dict[i])
        return stack
