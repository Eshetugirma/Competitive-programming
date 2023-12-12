class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        memo = defaultdict(int)
        for i in range(len(nums)):
            memo[nums[i]] = i

        for val1,val2 in operations:
            nums[memo[val1]] = val2
            curr_index = memo[val1]
            del memo[val1]
            memo[val2] = curr_index
            
        return nums
        