class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sorted_list = []

        for num in nums:

            pos = bisect_left(sorted_list,num)

            if pos == len(sorted_list):
                sorted_list.append(num)
            else:
                sorted_list[pos] = num
                
        return len(sorted_list)