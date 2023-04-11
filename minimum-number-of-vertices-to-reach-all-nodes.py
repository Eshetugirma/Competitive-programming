class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = set()
        res = []
        for i in range(len(edges)):
            ans.add(edges[i][1])
        for i in range(n):
            if i not in ans:
                res.append(i)
        return res