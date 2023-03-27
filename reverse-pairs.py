from sortedcontainers import SortedList
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        seen = SortedList()
        #===>>> this is just simple binary search on sorted list for those seen before
        for num in nums:
            count += len(seen) - bisect_right(seen,num*2) 
            seen.add(num)
        return count