class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        from sortedcontainers import SortedList
        #===>>>> first open sortedlist function then find index closest to edge
        count = 0
        check = SortedList()
        for num in instructions:
            count += min(check.bisect_left(num),len(check)-check.bisect_right(num))
            check.add(num)
            count %=(10**9+7)

        return count