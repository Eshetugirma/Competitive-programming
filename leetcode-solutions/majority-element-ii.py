class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)//3
        ans = []
        for key,value in count.items():
            if value > n:
                ans.append(key)
        return ans