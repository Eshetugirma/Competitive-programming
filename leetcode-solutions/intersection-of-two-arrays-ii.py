class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        ans = []
        for k,v in count1.items():
            curr = min(v,count2[k])
            for i in range(curr):
                ans.append(k)

        return ans
        