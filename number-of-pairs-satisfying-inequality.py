from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        count = 0
        arr = []
        seen = SortedList()
        #===>>> append all difference of nums1 and nums2 in to arr 
        for i in range(len(nums1)):
            arr.append(nums1[i]-nums2[i])
        #===>>> for all element in arr sort them in seen and take their index as count
        for num in arr:
            count += bisect_right(seen,num+diff)
            seen.add(num)
        return count