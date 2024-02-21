class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # print(intervals)
        stack = [intervals[0]]
        for pair in intervals:
            if stack[-1][1] >= pair[0] and pair[0] >= stack[-1][0]:
                stack[-1] = [stack[-1][0],max(pair[1],stack[-1][1])]
            else:
                stack.append(pair)
        return stack
        