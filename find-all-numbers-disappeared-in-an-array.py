class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        i = 0
        while i < len(nums):
            #===>>>> this to in-place all number in list to their correct position
            if nums[i] != i + 1 and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
            else:
                i += 1
        ans = []
        #==>> if any number in corrected list is not at his position then there is no number at that postion then append it to ans
        for i in range(len(nums)):
            if nums[i] != i + 1:
                ans.append(i + 1)
        return ans