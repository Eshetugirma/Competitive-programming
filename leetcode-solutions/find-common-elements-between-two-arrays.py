class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0,0]
        count1, count2 = Counter(nums1),Counter(nums2)
        for k,v in count1.items():
            if k in count2:
                ans[0] += v
                ans[1] += count2[k]
        return ans