class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums                   # =>transfer to other arr
        for i in range(n):
            string = str(nums[i])    # => change int in arr to string 
            reverse = string[::-1]   # =>reverse string by slice 
            ans.append(int(reverse)) # =>append reversed array in to new array
        return len(set(ans))         # =>change new array in to set then return its length 