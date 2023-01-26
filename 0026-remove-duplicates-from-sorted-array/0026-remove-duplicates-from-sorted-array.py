class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        place_holder = 1
        for seeker in range(len(nums)-1):
            if nums[seeker] != nums[seeker+1]:
                nums[place_holder] = nums[seeker+1]
                place_holder += 1
        return place_holder
        