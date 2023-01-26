class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0
        while pointer < len(nums)-1:
            if nums[pointer] == nums[pointer+1]:
                nums.remove(nums[pointer])
            else:
                pointer +=1
        print(nums)
        
        