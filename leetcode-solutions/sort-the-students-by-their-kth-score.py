class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        res = sorted(score,key = lambda x:x[k],reverse=True)
        return res