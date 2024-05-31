class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []
        dic = Counter(nums)
        for i in dic:
            if dic[i] == 1:
                ans.append(i)
            if len(ans) == 2:
                return ans