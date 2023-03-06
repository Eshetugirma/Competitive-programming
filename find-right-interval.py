class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        #==>> separate end and start 
        starts = [intervals[i][0] for i in range(len(intervals))]
        ends = [intervals[i][1] for i in range(len(intervals))]
        ans = []
        #==>>> sort starts and find index of right interval by using by bisect_left
        start_sorted = sorted(starts)
        for end in ends:
            ind = bisect_left(start_sorted,end)
            if ind == len(starts):
                ans.append(-1)
            else:
                i = starts.index(start_sorted[ind])
                ans.append(i)
        
        return ans