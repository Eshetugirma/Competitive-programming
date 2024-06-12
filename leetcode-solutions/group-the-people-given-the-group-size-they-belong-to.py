class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        indexed = []
        for i in range(n):
            indexed.append([groupSizes[i],i])
        indexed.sort()
        ans = []
        curr = []
        for i in range(n):
            curr.append(indexed[i][1])
            if len(curr) == indexed[i][0]:
                ans.append(curr)
                curr = []
        return ans





















