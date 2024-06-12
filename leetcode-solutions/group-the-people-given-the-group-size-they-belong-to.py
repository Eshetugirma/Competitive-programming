class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        indexed = []
        for i in range(n):
            indexed.append([groupSizes[i],i])
        indexed.sort()
        ans = []
        curr = []
        count = 0
        for i in range(n):
            curr.append(indexed[i][1])
            count += 1
            if count == indexed[i][0]:
                ans.append(curr)
                curr = []
                count = 0
        return ans





















